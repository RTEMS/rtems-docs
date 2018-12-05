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

import latex

sphinx_min_version = (1, 3)

def build_date():
    import datetime
    now = datetime.date.today()
    m = now.strftime('%B')
    y = now.strftime('%Y')
    if now.day % 10 == 1:
        s = 'st'
    elif now.day % 10 == 2:
        s = 'nd'
    elif now.day == 3:
        s = 'rd'
    else:
        s = 'th'
    d = '%2d%s' % (now.day, s)
    return '%s %s %s' % (d, m, y)

def version_cmdline(ctx):
    return '-Drelease="%s" -Dversion="%s"' % (ctx.env.VERSION, ctx.env.VERSION)

def sphinx_cmdline(ctx, build_type, conf_dir, doctrees,
                   source_dir, output_dir, configs = []):
    cfgs = ''
    for c in configs:
        cfgs += ' -D %s=%s' % (c, configs[c])
    rule = "${BIN_SPHINX_BUILD} %s -b %s -c %s %s -d %s %s %s %s ${SRC}" % \
           (sphinx_verbose(ctx), build_type, conf_dir, version_cmdline(ctx),
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
        source = ctx.path.ant_glob('**/*.rst'),
        target = "linkcheck/output.txt"
    )

class spell(BuildContext):
    __doc__ = "Check spelling.  Supply a list of files or a glob (*.rst)"
    cmd = 'spell'
    fun = 'cmd_spell'

class linkcheck(BuildContext):
    __doc__ = "Check all external URL references."
    cmd = 'linkcheck'
    fun = 'cmd_linkcheck'

def check_sphinx_version(ctx, minver):
    try:
        import sphinx
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
            ver = tuple(map(int, re.split('[\D]', version)))
        except:
            try:
                # sphinx-build returns its version info in stdout
                version = ctx.cmd_and_log(ctx.env.BIN_SPHINX_BUILD +
                              ['--version']).split(" ")[-1:][0].strip()
                try:
                    ver = tuple(map(int, re.split('[\D]', version)))
                except:
                    ctx.fatal("Sphinx version cannot be checked or Sphinx is not installed")
            except:
                ctx.fatal("Sphinx version cannot be checked or Sphinx is not installed")
    if ver < minver:
        ctx.fatal("Sphinx version is too old: %s" % ".".join(map(str, ver)))
    return ver

def sphinx_verbose(ctx):
    return ' '.join(ctx.env.SPHINX_VERBOSE)

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

def pdf_resources(ctx, buildtype):
    packages_base = ctx.path.parent.find_dir('common/latex')
    if packages_base is None:
        ctx.fatal('Latex package directory not found')
    base = packages_base.path_from(ctx.path)
    fnode = ctx.path.get_bld().make_node(buildtype)
    fnode.mkdir()
    local_packages = latex.local_packages()
    targets = []
    if local_packages is not None:
        srcs = [os.path.join(base, p) for p in local_packages]
        targets += [fnode.make_node(p) for p in local_packages]
        ctx(features = "subst",
            is_copy  = True,
            source   = srcs,
            target   = targets)
    targets += [fnode.make_node('rtemsextrafonts.sty')]
    ctx(features = "subst",
        is_copy  = True,
        source   = os.path.join(base, ctx.env.RTEMSEXTRAFONTS),
        target   = fnode.make_node('rtemsextrafonts.sty'))
    return targets

def html_resources(ctx, buildtype):
    extra_source = []
    for dir_name in ["_static", "_templates"]:
        files = ctx.path.parent.find_node("common").ant_glob("%s/*" % dir_name)
        fnode = ctx.path.get_bld().make_node(os.path.join(buildtype, dir_name))
        targets = [fnode.make_node(x.name) for x in files]
        extra_source += targets
        fnode.mkdir() # dirs
        ctx(features = "subst",
            is_copy  = True,
            source   = files,
            target   = targets)
        ctx.add_group()
    return extra_source

def check_sphinx_extension(ctx, extension):
    def run_sphinx(bld):
        rst_node = bld.srcnode.make_node('testbuild/contents.rst')
        rst_node.parent.mkdir()
        rst_node.write('.. COMMENT test sphinx\n')
        bld(rule = bld.kw['rule'], source = rst_node)

    ctx.start_msg("Checking for '%s'" % (extension))
    try:
        ctx.run_build(fragment = 'xx',
                      rule = "${BIN_SPHINX_BUILD} -b html -D extensions=%s -C . out" % (extension),
                      build_fun = run_sphinx,
                      env = ctx.env)
    except ctx.errors.ConfigurationError:
        ctx.end_msg('not found (see README.txt)', 'RED')
        ctx.fatal('The configuration failed')
    ctx.end_msg('found')

def cmd_configure(ctx):
    check_sphinx = not ctx.env.BIN_SPHINX_BUILD
    if check_sphinx:
        ctx.msg('Checking version', ctx.env.VERSION)

        ctx.find_program("sphinx-build", var="BIN_SPHINX_BUILD", mandatory = True)
        ctx.find_program("aspell", var = "BIN_ASPELL", mandatory = False)

        ctx.start_msg("Checking if Sphinx is at least %s.%s" % sphinx_min_version)
        ver = check_sphinx_version(ctx, sphinx_min_version)
        ctx.end_msg("yes (%s)" % ".".join(map(str, ver)))

        ctx.start_msg("Checking Sphinx Verbose ")
        if 'SPHINX_VERBOSE' not in ctx.env:
            ctx.env.append_value('SPHINX_VERBOSE', ctx.options.sphinx_verbose)
            level = sphinx_verbose(ctx)
            if level == '-Q':
                level = 'quiet'
            ctx.end_msg(level)
        #
        # Check extensions.
        #
        check_sphinx_extension(ctx, 'sphinx.ext.autodoc')
        check_sphinx_extension(ctx, 'sphinx.ext.coverage')
        check_sphinx_extension(ctx, 'sphinx.ext.doctest')
        check_sphinx_extension(ctx, 'sphinx.ext.graphviz')
        check_sphinx_extension(ctx, 'sphinx.ext.intersphinx')
        check_sphinx_extension(ctx, 'sphinx.ext.mathjax')
        check_sphinx_extension(ctx, 'sphinxcontrib.bibtex')

    #
    # Optional builds.
    #
    ctx.env.BUILD_PDF = 'no'
    if ctx.options.pdf:
        check_tex = not ctx.env.PDFLATEX
        if check_tex:
            ctx.load('tex')
            if not ctx.env.PDFLATEX or not ctx.env.MAKEINDEX:
                ctx.fatal('The programs pdflatex and makeindex are required for PDF output')
            if 'PDFLATEXFLAGS' not in ctx.env or \
               '-shell-escape' not in ctx.env['PDFLATEXFLAGS']:
                ctx.env.append_value('PDFLATEXFLAGS', '-shell-escape')
            latex.configure_tests(ctx)
        ctx.env.BUILD_PDF = 'yes'

    ctx.envBUILD_SINGLEHTML = 'no'
    if ctx.options.singlehtml:
        check_inliner = not ctx.env.BIN_INLINER
        if check_inliner:
            ctx.env.BUILD_SINGLEHTML = 'yes'
            ctx.find_program("inliner", var = "BIN_INLINER", mandatory = False)
            if not ctx.env.BIN_INLINER:
                ctx.fatal("Node.js inliner is required install with 'npm install -g inliner' " +
                          "(https://github.com/remy/inliner)")

    ctx.envBUILD_PLANTUML = 'no'
    if ctx.options.plantuml:
        check_plantuml = not ctx.env.BIN_PUML
        if check_plantuml:
            ctx.env.BUILD_PLANTUML = 'yes'
            ctx.find_program("puml", var = "BIN_PUML", mandatory = False)
            if not ctx.env.BIN_PUML:
                ctx.fatal("Node.js puml is required install with 'npm install -g node-plantuml' " +
                          "(https://www.npmjs.com/package/node-plantuml)")

    ctx.envBUILD_DITAA = 'no'
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
            ctx.env.BUILD_DITAA = 'yes'
            ctx.find_program("ditaa", var = "BIN_DITAA", mandatory = False)
            if not ctx.env.BIN_DITAA:
                ctx.fatal("DITAA not found, plase install")

def doc_pdf(ctx, source_dir, conf_dir, extra_source):
    buildtype = 'latex'
    build_dir, output_node, output_dir, doctrees = build_dir_setup(ctx, buildtype)
    resources = pdf_resources(ctx, buildtype)
    rule = sphinx_cmdline(ctx, buildtype, conf_dir, doctrees, source_dir, output_dir)
    ctx(
        rule         = rule,
        cwd          = ctx.path,
        source       = ctx.path.ant_glob('**/*.rst') + extra_source,
        depends_on   = extra_source,
        target       = ctx.path.find_or_declare("%s/%s.tex" % (buildtype,
                                                               ctx.path.name))
    )
    ctx(
        features     = 'tex',
        cwd          = output_dir,
        type         = 'pdflatex',
        source       = "%s/%s.tex" % (buildtype, ctx.path.name),
        prompt       = 0
    )
    ctx.install_files('${PREFIX}',
                      '%s/%s.pdf' % (buildtype, ctx.path.name),
                      cwd = output_node,
                      quiet = True)

def doc_singlehtml(ctx, source_dir, conf_dir, extra_source):
    #
    # Use a run command to handle stdout and stderr output from inliner. Using
    # a standard rule in the build context locks up.
    #
    def run(task):
        src = task.inputs[0].abspath()
        tgt = task.outputs[0].abspath()
        cmd = '%s %s' % (task.env.BIN_INLINER[0], src)
        so = open(tgt, 'w')
        se = open(tgt + '.err', 'w')
        r = task.exec_command(cmd, stdout = so, stderr = se)
        so.close()
        se.close()
        #
        # The inliner does not handle internal href's correctly and places the
        # input's file name in the href. Strip these.
        #
        with open(tgt, 'r') as i:
            before = i.read()
            after = before.replace('index.html', '')
        i.close()
        with open(tgt, 'w') as o:
            o.write(after)
        o.close()
        return r

    buildtype = 'singlehtml'
    build_dir, output_node, output_dir, doctrees = build_dir_setup(ctx, buildtype)
    resources = html_resources(ctx, buildtype)
    rule = sphinx_cmdline(ctx, buildtype, conf_dir, doctrees, source_dir, output_dir)
    ctx(
        rule         = rule,
        cwd          = ctx.path,
        source       = ctx.path.ant_glob('**/*.rst') + extra_source,
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

def doc_html(ctx, source_dir, conf_dir, extra_source):
    buildtype = 'html'
    build_dir, output_node, output_dir, doctrees = build_dir_setup(ctx, buildtype)
    resources = html_resources(ctx, buildtype)
    templates = os.path.join(str(ctx.path.get_bld()), buildtype, '_templates')
    configs = { 'templates_path': templates }
    rule = sphinx_cmdline(ctx, buildtype, conf_dir, doctrees, source_dir, output_dir, configs)
    ctx(
        rule         = rule,
        cwd          = ctx.path,
        source       = ctx.path.ant_glob('**/*.rst') + extra_source,
        depends_on   = resources,
        target       = ctx.path.find_or_declare('%s/index.html' % buildtype),
        install_path = None
    )
    ctx.install_files('${PREFIX}/%s' % (ctx.path.name),
                      output_node.ant_glob('**/*', quiet = True),
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
        tgt = src.abspath()[: - len(ext)] + '.png'
        ctx(
            rule         = run,
            inliner      = ctx.env.BIN_PUML,
            source       = src,
            target       = tgt,
            install_path = None
    )


def cmd_build(ctx, extra_source = []):
    conf_dir = ctx.path.get_src()
    source_dir = ctx.path.get_src()

    if ctx.env.BUILD_PDF == 'yes':
        doc_pdf(ctx, source_dir, conf_dir, extra_source)

    if ctx.env.BUILD_SINGLEHTML == 'yes':
        doc_singlehtml(ctx, source_dir, conf_dir, extra_source)

    doc_html(ctx, source_dir, conf_dir, extra_source)

def cmd_build_images(ctx):
    conf_dir = ctx.path.get_src()
    source_dir = ctx.path.get_src()
    if ctx.env.BUILD_PLANTUML == 'yes':
        images_plantuml(ctx, source_dir, conf_dir, '.puml')
    if ctx.env.BUILD_DITAA == 'yes':
        images_plantuml(ctx, source_dir, conf_dir, '.ditaa')

def cmd_options(ctx):
    ctx.add_option('--disable-extra-fonts',
                   action = 'store_true',
                   default = False,
                   help = "Disable building with extra fonts for better quality (lower quality).")
    ctx.add_option('--sphinx-verbose',
                   action = 'store',
                   default = "-Q",
                   help = "Sphinx verbose.")
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
    sp = sys.path[:]
    for doc in building:
        #
        # Import using the imp API so the module is reloaded for us.
        #
        import imp
	sys.path = [top_dir.find_node(doc).abspath()]
        mf = imp.find_module('conf')
        sys.path = sp[:]
        try:
            bconf = imp.load_module('bconf', mf[0], mf[1], mf[2])
        finally:
            mf[0].close()
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
    root.setAttribute('date', build_date())
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
