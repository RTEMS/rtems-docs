#
# RTEMS Documentation Project
#
# Waf build support.
#


from __future__ import print_function

import os
import re
import sys

from waflib.Build import BuildContext
from waflib.TaskGen import feature, before_method, after_method

import latex
import conf

import os
import subprocess

windows = os.name == 'nt'

# If you do not want to check for a maximum version, set it to None.
sphinx_min_version = (1, 3)
sphinx_max_version = None

def version_cmdline(ctx):
    if ctx.env.RTEMS_RELEASED:
        DROPDOWN_VERSION = ctx.env.VERSION
    else:
        DROPDOWN_VERSION = "main"

    return '-Drelease="%s" -Dversion="%s" -Drtems_major="%s" ' \
           '-Drtems_minor="%s" -D rtems_revision="%s" -Dhtml_theme_logo.text="%s" -Dhtml_theme_version_switcher.version_match="%s"' \
        % (ctx.env.RELEASE, ctx.env.VERSION, ctx.env.RTEMS_MAJOR,
           ctx.env.RTEMS_MINOR, ctx.env.RTEMS_REVISION, ctx.env.VERSION, DROPDOWN_VERSION)

def sphinx_cmdline(ctx, build_type, conf_dir, doctrees,
                   source_dir, output_dir, configs = []):
    cfgs = ''
    for c in configs:
        cfgs += ' -D %s=%s' % (c, configs[c])
    rule = "${BIN_SPHINX_BUILD} %s -b %s -c %s %s -d %s %s %s %s ${SRC}" % \
           (sphinx_options(ctx), build_type, conf_dir, version_cmdline(ctx),
            doctrees, cfgs, source_dir, output_dir)
    return rule

def cmd_spell(ctx):
    from waflib import Options
    from sys import argv
    from subprocess import call

    Options.commands = None # stop warnings about knowing commands.

    if not ctx.env.BIN_ASPELL:
        ctx.fatal("'aspell' is required please install and re-run configure.")

    if len(argv) < 3:
        ctx.fatal("Please supply at least one file name")

    files = argv[2:]

    path = ctx.path.parent.abspath()

    # XXX: add error checking eg check if file exists.
    for file in files:
        cmd = ctx.env.BIN_ASPELL + \
              ["-c",
               "--personal=%s/common/spell/dict/rtems" % path,
               "--extra-dicts=%s/common/spell/en_GB-ise-w_accents.multi" % path,
               file]
        print("running:", cmd)
        call(cmd)

def cmd_linkcheck(ctx):
    conf_dir = ctx.path.get_src()
    source_dir = ctx.path.get_src()
    buildtype = 'linkcheck'
    build_dir, output_node, output_dir, doctrees = build_dir_setup(ctx, buildtype)
    rule = sphinx_cmdline(ctx, buildtype, conf_dir, doctrees, source_dir, output_dir)
    ctx(
        rule   = rule,
        cwd    = ctx.path.abspath(),
        source = ctx.path.ant_glob('**/*.md'),
        target = "linkcheck/output.txt"
    )

class spell(BuildContext):
    __doc__ = "Check spelling.  Supply a list of files or a glob (*.md)"
    cmd = 'spell'
    fun = 'cmd_spell'

class linkcheck(BuildContext):
    __doc__ = "Check all external URL references."
    cmd = 'linkcheck'
    fun = 'cmd_linkcheck'

def check_sphinx_version(ctx, minver, maxver):
    try:
        import sphinx
    except:
        ctx.fatal('no sphinx support found; please install')
    try:
        # sphinx.version_info was introduced in sphinx ver 1.2
        version = sphinx.version_info
        # version looks like (1, 7, 0, 'final', 0))
        ver = version[0:2]
    except:
        try:
            # sphinx-build returns its version info in stderr
            (out, err) = ctx.cmd_and_log(ctx.env.BIN_SPHINX_BUILD +
                              ['--version'], output=Context.BOTH)
            # err looks like 'sphinx-build 1.7.0\n'
            version = err.split(" ")[-1:][0].strip()
            ver = tuple(map(int, re.split(r'[\D]', version)))
        except:
            try:
                # sphinx-build returns its version info in stdout
                version = ctx.cmd_and_log(ctx.env.BIN_SPHINX_BUILD +
                              ['--version']).split(" ")[-1:][0].strip()
                try:
                    ver = tuple(map(int, re.split(r'[\D]', version)))
                except:
                    ctx.fatal("Sphinx version cannot be checked or Sphinx is not installed")
            except:
                ctx.fatal("Sphinx version cannot be checked or Sphinx is not installed")
    if ver < minver:
        ctx.fatal("Sphinx version is too old: %s" % ".".join(map(str, ver)))
    if maxver is not None:
        if ver > maxver:
            ctx.fatal("Sphinx version is too new: %s" % ".".join(map(str, ver)))
    return ver

def sphinx_options(ctx):
    return ' '.join(ctx.env.SPHINX_OPTIONS)

def is_top_build(ctx):
    from_top = False
    if ctx.env['BUILD_FROM_TOP'] and ctx.env['BUILD_FROM_TOP'] == 'yes':
        from_top = True
    return from_top

def build_dir_setup(ctx, buildtype):
    where = buildtype
    if is_top_build(ctx):
        where = os.path.join(ctx.path.name, where)
    bnode = ctx.bldnode.find_node(where)
    if bnode is None:
        ctx.bldnode.make_node(where).mkdir()
    build_dir = ctx.path.get_bld().relpath()
    output_node = ctx.path.get_bld().make_node(buildtype)
    output_dir = output_node.abspath()
    doctrees = os.path.join(os.path.dirname(output_dir), 'doctrees', buildtype)
    return build_dir, output_node, output_dir, doctrees

def pdf_resources(ctx, buildtype, book):
    packages_base = ctx.path.parent.find_dir('common/latex')
    if packages_base is None:
        ctx.fatal('Latex package directory not found')
    base = packages_base.path_from(ctx.path)
    fnode = ctx.path.get_bld().make_node(buildtype)
    fnode.mkdir()
    targets = []
    name = 'pdf-' + book,
    targets += [fnode.make_node('rtemsextrafonts.sty')]
    ctx(features = "subst",
        name     = name,
        is_copy  = True,
        source   = os.path.join(base, ctx.env.RTEMSEXTRAFONTS),
        target   = fnode.make_node('rtemsextrafonts.sty'))
    return name

def html_resources(ctx, buildtype, book):
    resources = []
    for dir_name in ["_static", "_templates"]:
        files = ctx.path.parent.find_node("common").ant_glob("%s/*" % dir_name)
        fnode = ctx.path.get_bld().make_node(os.path.join(buildtype, dir_name))
        targets = [fnode.make_node(x.name) for x in files]
        resources += targets
        name = 'html-' + book
        fnode.mkdir() # dirs
        ctx(features = "subst",
            name = name,
            is_copy  = True,
            source   = files,
            target   = targets)
    return name

def check_sphinx_extension(ctx, extension):
    def run_sphinx(bld):
        md_node = bld.srcnode.make_node('testbuild/contents.rst')
        md_node.parent.mkdir()
        md_node.write('.. COMMENT test sphinx' + os.linesep)
        bib_node = bld.srcnode.make_node('testbuild/refs.bib')
        bib_node.write(os.linesep)
        conf_node = bld.srcnode.make_node('testbuild/conf.py')
        conf_node.write(os.linesep.join(["master_doc='contents'",
                                         "bibtex_bibfiles = ['refs.bib']"]))
        bld(rule = bld.kw['rule'], source = md_node)

    ctx.start_msg("Checking for '%s'" % (extension))
    try:
        ctx.run_build(fragment = 'xx',
                      rule = "${BIN_SPHINX_BUILD} -b html -D extensions=%s -c . . out" % (extension),
                      build_fun = run_sphinx,
                      env = ctx.env)
    except ctx.errors.ConfigurationError:
        ctx.end_msg('not found (see README.txt)', 'RED')
        ctx.fatal('The configuration failed')
    ctx.end_msg('found')

def check_sphinx_theme(ctx, theme):
    def run_sphinx(bld):
        md_node = bld.srcnode.make_node('testbuild/contents.md')
        md_node.parent.mkdir()
        md_node.write('.. COMMENT test sphinx' + os.linesep)
        bib_node = bld.srcnode.make_node('testbuild/refs.bib')
        bib_node.write(os.linesep)
        conf_node = bld.srcnode.make_node('testbuild/conf.py')
        conf_node.write(os.linesep.join(["master_doc='contents'",
                                         "bibtex_bibfiles = ['refs.bib']"]))
        bld(rule = bld.kw['rule'], source = md_node)

    ctx.start_msg("Checking for '%s'" % (theme))
    try:
        theme__ = theme.replace('-', '_')
        bld_rule = '${BIN_SPHINX_BUILD} -b html -c . '
        bld_rule += '-D html_theme=%s ' % (theme__)
        bld_rule += '-D "html_them_path=[%s.get_html_theme_path()]" ' % (theme__)
        bld_rule += '. out'
        ctx.run_build(fragment = 'xx',
                      rule = bld_rule,
                      build_fun = run_sphinx,
                      env = ctx.env)
    except ctx.errors.ConfigurationError:
        ctx.end_msg('not found (see README.txt)', 'RED')
        ctx.fatal('The configuration failed')
    ctx.end_msg('found')

def cmd_configure(ctx):
    ctx.env.DOC_LIST = ctx.options.doc_list[0].split(
        ",") if ctx.options.doc_list else []
    ctx.env.PYTHON = ["python3"]
    ctx.check_python_version((3,9))
    ctx.load("python")
    check_sphinx = not ctx.env.BIN_SPHINX_BUILD
    if check_sphinx:
        ctx.find_program("sphinx-build", var="BIN_SPHINX_BUILD", mandatory = True)
        ctx.find_program("aspell", var = "BIN_ASPELL", mandatory = False)

        if sphinx_max_version is None:
          ctx.start_msg("Checking if Sphinx is at least %s.%s" % sphinx_min_version)
        else:
          ctx.start_msg("Checking if Sphinx is between %s.%s and %s.%s" % (sphinx_min_version + sphinx_max_version))

        ver = check_sphinx_version(ctx, sphinx_min_version, sphinx_max_version)
        ctx.end_msg("yes (%s)" % ".".join(map(str, ver)))

        ctx.start_msg("Checking Sphinx Options ")
        if 'SPHINX_OPTIONS' not in ctx.env:
            ctx.env.append_value('SPHINX_OPTIONS', ctx.options.sphinx_options)
            opts = sphinx_options(ctx)
            if len(opts) == 0:
                opts = 'none'
            ctx.end_msg(opts)

        ctx.start_msg("Checking Sphinx Nit-Pick mode ")
        if ctx.options.sphinx_nit_pick:
            opt = '-n'
            msg = 'yes'
        else:
            opt = '-Q'
            msg = 'no'
        ctx.env.append_value('SPHINX_OPTIONS', opt)
        ctx.end_msg(msg)

        # FIXME: Checking for the Python module is broken on MSYS2
        if not windows:
            ctx.check_python_module('sphinx_book_theme')
            ctx.check_python_module('sphinx_copybutton')
            ctx.check_python_module('linkify_it')
            ctx.check_python_module('myst_parser')
            ctx.check_python_module('sphinx_design')
            ctx.check_python_module('sphinx_tippy')
            ctx.check_python_module('sphinx_togglebutton')
            ctx.check_python_module('sphinxext.opengraph')
        else:
            pass



        #
        # Check extensions.
        #
#        check_sphinx_extension(ctx, 'sphinx.ext.autodoc')
        check_sphinx_extension(ctx, 'sphinx.ext.coverage')
        check_sphinx_extension(ctx, 'sphinx.ext.doctest')
        check_sphinx_extension(ctx, 'sphinx.ext.graphviz')
        check_sphinx_extension(ctx, 'sphinx.ext.intersphinx')
        check_sphinx_extension(ctx, 'sphinx.ext.mathjax')
        check_sphinx_extension(ctx, 'sphinxcontrib.bibtex')
        check_sphinx_extension(ctx, 'sphinx_copybutton')
        check_sphinx_extension(ctx, 'sphinxcontrib.jquery')
        check_sphinx_extension(ctx, 'myst_parser')
        check_sphinx_extension(ctx, 'sphinx_design')
        check_sphinx_extension(ctx, 'sphinx_tippy')
        check_sphinx_extension(ctx, 'sphinx_togglebutton')
        check_sphinx_extension(ctx, 'sphinxext.opengraph')


    #
    # Optional builds.
    #
    ctx.env.BUILD_PDF = 'no'
    if ctx.options.pdf:
        if conf.latex_engine == 'xelatex':
            if not ctx.env.LATEX_CMD:
                ctx.load('tex')
                if not ctx.env.XELATEX or not ctx.env.MAKEINDEX:
                    ctx.fatal('The programs xelatex and makeindex are required for PDF output')
                ctx.env.LATEX_CMD = 'xelatex'
                latex.configure_tests(ctx)
                # Minted needs 'shell-escape'
                if 'XELATEXFLAGS' not in ctx.env or \
                   '-shell-escape' not in ctx.env['XELATEXFLAGS']:
                    ctx.env.append_value('XELATEXFLAGS', '-shell-escape')
                ctx.env.append_value('MAKEINDEXFLAGS', ['-s', 'python.ist'])
        elif conf.latex_engine == 'pdflatex':
            if not ctx.env.LATEX_CMD:
                ctx.load('tex')
                if not ctx.env.PDFLATEX or not ctx.env.MAKEINDEX:
                    ctx.fatal('The programs pdflatex and makeindex are required for PDF output')
                if 'PDFLATEXFLAGS' not in ctx.env or \
                   '-shell-escape' not in ctx.env['PDFLATEXFLAGS']:
                    ctx.env.append_value('PDFLATEXFLAGS', '-shell-escape')
                ctx.env.append_value('MAKEINDEXFLAGS', ['-s', 'python.ist'])
                ctx.env.LATEX_CMD = 'pdflatex'
                latex.configure_tests(ctx)
        else:
            ctx.fatal('Unsupported latex engine: %s' % (conf.latex_engine))
        ctx.env.BUILD_PDF = 'yes'

    ctx.env.BUILD_SINGLEHTML = 'no'
    if ctx.options.singlehtml:
        check_inliner = not ctx.env.BIN_INLINER
        if check_inliner:
            ctx.find_program("inliner", var = "BIN_INLINER", mandatory = False)
            if not ctx.env.BIN_INLINER:
                ctx.fatal("Node.js inliner is required install with 'npm install -g inliner' " +
                          "(https://github.com/remy/inliner)")
        ctx.env.BUILD_SINGLEHTML = 'yes'

    ctx.env.BUILD_PLANTUML = 'no'
    if ctx.options.plantuml:
        check_plantuml = not ctx.env.BIN_PUML
        if check_plantuml:
            ctx.find_program("puml", var = "BIN_PUML", mandatory = False)
            if not ctx.env.BIN_PUML:
                ctx.fatal("Node.js puml is required install with 'npm install -g node-plantuml' " +
                          "(https://www.npmjs.com/package/node-plantuml)")
        ctx.env.BUILD_PLANTUML = 'yes'

    ctx.env.BUILD_DITAA = 'no'
    if ctx.options.ditaa:
        #
        # We use DITAA via PlantUML
        #
        if not ctx.env.BIN_PUML:
            ctx.find_program("puml", var = "BIN_PUML", mandatory = False)
            if not ctx.env.BIN_PUML:
                ctx.fatal("DITAA uses PlantUML; " +
                          "Node.js puml is required install with 'npm install -g node-plantuml' " +
                          "(https://www.npmjs.com/package/node-plantuml)")
        check_ditaa = not ctx.env.BIN_DITAA
        if check_ditaa:
            ctx.find_program("ditaa", var = "BIN_DITAA", mandatory = False)
            if not ctx.env.BIN_DITAA:
                ctx.fatal("DITAA not found, plase install")
        ctx.env.BUILD_DITAA = 'yes'

def sources_exclude(ctx, sources):
    exclude = sources.get('exclude', [])
    if len(exclude) == 0:
        return exclude
    return [ctx.path.find_node(e) for e in exclude]

def sources_extra(ctx, sources):
    extra = sources.get('extra', [])
    if len(extra) == 0:
        extra = [ctx.path.find_node(e) for e in extra]
    return [e for e in extra if e not in sources_exclude(ctx, sources)]

def sources_source(ctx, sources):
    extra = sources_extra(ctx, sources)
    exclude = sources_exclude(ctx, sources)
    source = ctx.path.ant_glob('**/*.md')
    return [s for s in source if s not in exclude] + extra

def doc_pdf(ctx, source_dir, conf_dir, sources):
    book = os.path.basename(source_dir.abspath())
    buildtype = 'latex'
    build_dir, output_node, output_dir, doctrees = build_dir_setup(ctx, buildtype)
    resources = pdf_resources(ctx, buildtype, book)
    rule = sphinx_cmdline(ctx, buildtype, conf_dir, doctrees, source_dir, output_dir)
    ctx(
        rule         = rule,
        cwd          = ctx.path,
        source       = sources_source(ctx, sources),
        depends_on   = [resources] + sources_extra(ctx, sources),
        target       = ctx.path.find_or_declare("%s/%s.tex" % (buildtype,
                                                               ctx.path.name))
    )
    env_latex = ctx.env.derive()
    env_latex.TEXINPUTS = output_dir + ':'
    ctx(
        features     = 'tex',
        cwd          = output_dir,
        type         = ctx.env.LATEX_CMD,
        source       = "%s/%s.tex" % (buildtype, ctx.path.name),
        prompt       = 0,
        env          = env_latex,
        depends_on   = resources
    )
    ctx.install_files('${PREFIX}',
                      '%s/%s.pdf' % (buildtype, ctx.path.name),
                      cwd = output_node,
                      quiet = True)

def doc_singlehtml(ctx, source_dir, conf_dir, sources):
    #
    # Use a run command to handle stdout and stderr output from inliner. Using
    # a standard rule in the build context locks up.
    #
    def run(task):
        src = task.inputs[0].abspath()
        tgt = task.outputs[0].abspath()
        cmd = '%s %s' % (task.env.BIN_INLINER[0], src)
        so = open(tgt, 'w')
        se = open("{}_stderr".format(tgt), 'w')

        # inliner does not handle digests and fails to open the file.
        with open(src, "rb") as fp:
            no_hash = re.sub(b'\\?v=[a-z0-9]{8}', b'', fp.read())
            no_digest = re.sub(b'\\?digest=[a-z0-9]{20}', b'', no_hash)
        with open(src, "wb") as fp:
            fp.write(no_digest)

        r = task.exec_command(cmd, stdout = so, stderr = se, stdin=None)

        so.close()
        se.close()

        #
        # The inliner does not handle internal href's correctly and places the
        # input's file name in the href. Strip these.
        #
        if sys.version_info[0] < 3:
            with open(tgt, 'r') as i:
                before = i.read()
        else:
            with open(tgt, 'r', encoding = 'ascii', errors = 'surrogateescape') as i:
                before = i.read()
        i.close()
        after = before.replace('index.html', '')
        if sys.version_info[0] < 3:
            with open(tgt, 'w') as o:
                o.write(after)
        else:
            with open(tgt, 'w', encoding = 'ascii', errors = 'surrogateescape') as o:
                o.write(after)
        o.close()
        return r

    book = os.path.basename(source_dir.abspath())
    buildtype = 'singlehtml'
    build_dir, output_node, output_dir, doctrees = build_dir_setup(ctx, buildtype)
    resources = html_resources(ctx, buildtype, book)
    configs = { 'singlehtml_sidebars.index': "" }
    rule = sphinx_cmdline(ctx, buildtype, conf_dir, doctrees, source_dir, output_dir, configs)
    ctx(
        rule         = rule,
        cwd          = ctx.path,
        source       = sources_source(ctx, sources),
        depends_on   = resources,
        target       = ctx.path.find_or_declare("%s/index.html" % (buildtype)),
        install_path = None
    )
    ctx(
        rule         = run,
        inliner      = ctx.env.BIN_INLINER,
        source       = "%s/index.html" % buildtype,
        target       = "%s/%s.html" % (buildtype, ctx.path.name),
        install_path = '${PREFIX}'
    )

def doc_html(ctx, source_dir, conf_dir, sources):
    book = os.path.basename(source_dir.abspath())
    buildtype = 'html'
    build_dir, output_node, output_dir, doctrees = build_dir_setup(ctx, buildtype)
    resources =  html_resources(ctx, buildtype, book)
    templates = os.path.join(str(ctx.path.get_bld()), buildtype, '_templates')
    configs = { 'templates_path': templates, 'html_context.doc_path': book }
    rule = sphinx_cmdline(ctx, buildtype, conf_dir, doctrees, source_dir, output_dir, configs)
    ctx(
        rule         = rule,
        cwd          = ctx.path,
        source       = sources_source(ctx, sources),
        depends_on   = resources,
        target       = ctx.path.find_or_declare('%s/index.html' % buildtype),
        install_path = None
    )
    ctx.install_files('${PREFIX}/%s' % (ctx.path.name),
                      output_node.ant_glob('**/*', quiet = True, remove=False),
                      cwd = output_node,
                      relative_trick = True,
                      quiet = True)

def images_plantuml(ctx, source_dir, conf_dir, ext):
    #
    # Use a run command to handle stdout and stderr output from puml.
    #
    def run(task):
        src = task.inputs[0].abspath()
        tgt = task.outputs[0].abspath()
        cmd = '%s generate %s -o %s' % (task.env.BIN_PUML[0], src, tgt)
        so = open(tgt + '.out', 'w')
        r = task.exec_command(cmd, stdout = so, stderr = so)
        so.close()
        return r

    for src in ctx.path.ant_glob('**/*' + ext):
        tgt = src.change_ext('.png')
        ctx(
            rule         = run,
            inliner      = ctx.env.BIN_PUML,
            source       = src,
            target       = tgt,
            install_path = None
        )

def cmd_build(ctx, sources = {}, source_dir=None):

    conf_dir = ctx.path.get_src()
    if not source_dir:
        source_dir = ctx.path.get_src()

    if ctx.env.BUILD_PDF == 'yes':
        doc_pdf(ctx, source_dir, conf_dir, sources)

    if ctx.env.BUILD_SINGLEHTML == 'yes':
        doc_singlehtml(ctx, source_dir, conf_dir, sources)

    doc_html(ctx, source_dir, conf_dir, sources)

def cmd_build_images(ctx):
    conf_dir = ctx.path.get_src()
    source_dir = ctx.path.get_src()
    if ctx.env.BUILD_PLANTUML == 'yes':
        images_plantuml(ctx, source_dir, conf_dir, '.puml')
    if ctx.env.BUILD_DITAA == 'yes':
        images_plantuml(ctx, source_dir, conf_dir, '.ditaa')

@feature('deferred_doc_target_creation')
@before_method('process_source', 'process_rule')
def deferred_doc_target_creation(self):
    if self.sources_val.get('deferred_glob', None):
        found_nodes = self.path.get_bld().ant_glob(self.sources_val['deferred_glob'], remove=False)
        self.sources_val['extra'] = [x.path_from(self.path) for x in found_nodes]
    self.bld.path = self.path # hack, we are not traversing folders here

    source_dir = self.sources_val.get('source_dir', None)
    cmd_build(self.bld, self.sources_val, source_dir=source_dir)

@after_method('process_rules', 'process_source')
def force_dependency_on(self):
    if hasattr(self, 'depends_on'):
        node_list = self.to_nodes(self.to_list(self.depends_on))
        for task in self.tasks:
            task.add_manual_dependency(node_list)

def deferred_cmd_build(ctx, sources = {}):
    # assume one main build group for most targets such as file copies to the build directory
    if not ctx.groups:
        ctx.add_group(move=False)

    # second build group for sphinx targets
    try:
        ctx.add_group('doc_building', move=False)
    except Exception:
        pass

    # Add task generators in the second build group called 'doc_building'
    ctx(features='deferred_doc_target_creation', sources_val=sources, group='doc_building')

def cmd_options(ctx):
    ctx.load('python')
    ctx.add_option('--disable-extra-fonts',
                   action = 'store_true',
                   default = False,
                   help = "Disable building with extra fonts for better quality (lower quality).")
    ctx.add_option('--sphinx-options',
                   action = 'store',
                   default = "",
                   help = "Additional Sphinx options.")
    ctx.add_option('--sphinx-nit-pick',
                   action = 'store_true',
                   default = False,
                   help = "Enable Sphinx nit-picky mode else be quiet")
    ctx.add_option('--pdf',
                   action = 'store_true',
                   default = False,
                   help = "Build PDF.")
    ctx.add_option('--singlehtml',
                   action = 'store_true',
                   default = False,
                   help = "Build Single HTML file, requires Node Inliner")
    ctx.add_option('--plantuml',
                   action = 'store_true',
                   default = False,
                   help = "Build PlantUML images from source, need puml from npm")
    ctx.add_option('--ditaa',
                   action = 'store_true',
                   default = False,
                   help = "Build DITAA images using PlantUML from source, need ditaa and puml")
    ctx.add_option('--doc-list',
                   action = 'store',
                   default = "",
                   nargs="+",
                   help = "Comma separated list of docs to build.")

def cmd_options_path(ctx):
    cmd_options(ctx)
    ctx.add_option('--rtems-path-py',
                   type = 'string',
                   help = "Full path to py/ in RTEMS source repository.")

def cmd_configure_path(ctx):
    if not ctx.options.rtems_path_py:
        ctx.fatal("--rtems-path-py is required")

    ctx.env.RTEMS_PATH = ctx.options.rtems_path_py

    cmd_configure(ctx)

def xml_catalogue(ctx, building):
    #
    # The following is a hack to find the top_dir because the task does
    # provided a reference to top_dir like a build context.
    #
    top_dir = ctx.get_cwd().find_node('..')
    #
    # Read the conf.py files in each directory to gather the doc details.
    #
    catalogue = {}
    for doc in building:
        #
        # Import using the imp API so the module is reloaded for us.
        #
        import importlib
        p = os.path.join(top_dir.find_node(doc).abspath(), 'conf.py')
        mf = importlib.util.spec_from_file_location('conf', p)
        try:
            bconf = mf.loader.load_module()
        except (ValueError, ImportError) as exc:
            print("Import error " + str(exc))
            sys.exit(0)
        catalogue[doc] = {
            'title': bconf.project,
            'version': str(ctx.env.VERSION),
            'release': str(ctx.env.VERSION),
            'pdf': bconf.latex_documents[0][1].replace('.tex', '.pdf'),
            'html': '%s/index.html' % (doc),
            'singlehtml': '%s.html' % (doc)
        }
        bconf = None

    import xml.dom.minidom as xml
    cat = xml.Document()

    root = cat.createElement('rtems-docs')
    root.setAttribute('date', ctx.env.DATE)
    cat.appendChild(root)

    heading = cat.createElement('catalogue')
    text = cat.createTextNode(str(ctx.env.VERSION))
    heading.appendChild(text)
    root.appendChild(heading)

    builds = ['html']
    if ctx.env.BUILD_PDF == 'yes':
        builds += ['pdf']
    if ctx.env.BUILD_SINGLEHTML == 'yes':
        builds += ['singlehtml']

    for d in building:
        doc = cat.createElement('doc')
        name = cat.createElement('name')
        text = cat.createTextNode(d)
        name.appendChild(text)
        title = cat.createElement('title')
        text = cat.createTextNode(catalogue[d]['title'])
        title.appendChild(text)
        release = cat.createElement('release')
        text = cat.createTextNode(catalogue[d]['release'])
        release.appendChild(text)
        version = cat.createElement('version')
        text = cat.createTextNode(catalogue[d]['version'])
        version.appendChild(text)
        doc.appendChild(name)
        doc.appendChild(title)
        doc.appendChild(release)
        doc.appendChild(version)
        for b in builds:
            output = cat.createElement(b)
            text = cat.createTextNode(catalogue[d][b])
            output.appendChild(text)
            doc.appendChild(output)
        root.appendChild(doc)

    catnode = ctx.get_cwd().make_node('catalogue.xml')
    catnode.write(cat.toprettyxml(indent = ' ' * 2, newl = os.linesep))

    cat.unlink()
