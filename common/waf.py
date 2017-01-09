import sys, os, re
from waflib.Build import BuildContext

import latex

sphinx_min_version = (1, 3)

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


def cmd_linkcheck(ctx, conf_dir=".", source_dir="."):
    ctx_rule = "${BIN_SPHINX_BUILD} -b linkcheck -c %s -j %d " + \
               "-d build/doctrees %s build/linkcheck" % (conf_dir,
                                                         ctx.options.jobs,
                                                             source_dir)
    ctx(
        rule   = ctx_rule,
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
    version = ctx.cmd_and_log(ctx.env.BIN_SPHINX_BUILD +
                              ['--version']).split(" ")[-1:][0].strip()
    try:
        ver = tuple(map(int, re.split('[\D]', version)))
    except:
        ctx.fatal("Sphinx version cannot be checked: %s" % version)
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
    if local_packages is not None:
        srcs = [os.path.join(base, p) for p in local_packages]
        ctx(
            features = "subst",
            is_copy  = True,
            source   = srcs,
            target   = [fnode.make_node(p) for p in local_packages]
        )
    ctx(
        features = "subst",
        is_copy  = True,
        source   = os.path.join(base, ctx.env.RTEMSEXTRAFONTS),
        target   = fnode.make_node('rtemsextrafonts.sty')
    )

def html_resources(ctx, buildtype):
    for dir_name in ["_static", "_templates"]:
        files = ctx.path.parent.find_node("common").ant_glob("%s/*" % dir_name)
        fnode = ctx.path.get_bld().make_node(os.path.join(buildtype, dir_name))
        fnode.mkdir() # dirs
        ctx(
            features = "subst",
            is_copy  = True,
            source   = files,
            target   = [fnode.make_node(x.name) for x in files]
        )

    # copy images
#    ctx.path.get_bld().make_node("images").mkdir()
#    files = ctx.path.parent.ant_glob("images/**")
#    ctx(
#        features    = "subst",
#        is_copy     = True,
#        source      = files,
#        target      = [x.srcpath().replace("../", "") for x in files]
#    )


def cmd_configure(ctx):
    ctx.find_program("sphinx-build", var="BIN_SPHINX_BUILD", mandatory = True)
    ctx.find_program("aspell", var = "BIN_ASPELL", mandatory = False)

    ctx.start_msg("Checking if Sphinx is at least %s.%s" % sphinx_min_version)
    ver = check_sphinx_version(ctx, sphinx_min_version)
    ctx.end_msg("yes (%s)" % ".".join(map(str, ver)))

    ctx.start_msg("Sphinx Verbose: ")
    if 'SPHINX_VERBOSE' not in ctx.env:
        ctx.env.append_value('SPHINX_VERBOSE', ctx.options.sphinx_verbose)
    level = sphinx_verbose(ctx)
    if level == '-Q':
        level = 'quiet'
    ctx.end_msg(level)

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
        else:
            ctx.msg('Check for Tex packages', 'skipping, already checked')
        ctx.env.BUILD_PDF = 'yes'

    ctx.envBUILD_SINGLEHTML = 'no'
    if ctx.options.singlehtml:
        ctx.env.BUILD_SINGLEHTML = 'yes'
        ctx.find_program("inliner", var = "BIN_INLINER", mandatory = False)
        if not ctx.env.BIN_INLINER:
            ctx.fatal("Node inliner is required install with 'npm install -g inliner' " +
                      "(https://github.com/remy/inliner)")

def doc_pdf(ctx, source_dir, conf_dir):
    buildtype = 'latex'
    build_dir, output_node, output_dir, doctrees = build_dir_setup(ctx, buildtype)
    pdf_resources(ctx, buildtype)
    rule = "${BIN_SPHINX_BUILD} %s -b %s -c %s -d %s %s %s" % \
           (sphinx_verbose(ctx), buildtype, conf_dir,
            doctrees, source_dir, output_dir)
    ctx(
        rule         = rule,
        cwd          = ctx.path,
        source       = ctx.path.ant_glob('**/*.rst'),
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

def doc_singlehtml(ctx, source_dir, conf_dir):
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
    html_resources(ctx, buildtype)
    rule = "${BIN_SPHINX_BUILD} %s -b %s -c %s -d %s %s %s" % \
           (sphinx_verbose(ctx), buildtype, conf_dir,
            doctrees, source_dir, output_dir)
    ctx(
        rule         = rule,
        cwd          = ctx.path,
        source       = ctx.path.ant_glob('**/*.rst'),
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

def doc_html(ctx, conf_dir, source_dir):
    buildtype = 'html'
    build_dir, output_node, output_dir, doctrees = build_dir_setup(ctx, buildtype)
    html_resources(ctx, buildtype)
    rule = "${BIN_SPHINX_BUILD} %s -b %s -c %s -d %s %s %s" % \
           (sphinx_verbose(ctx), buildtype, conf_dir,
            doctrees, source_dir, output_dir)
    ctx(
        rule         = rule,
        cwd          = ctx.path,
        source       = ctx.path.ant_glob('**/*.rst'),
        target       = ctx.path.find_or_declare('%s/index.html' % buildtype),
        install_path = None
    )
    ctx.install_files('${PREFIX}/%s' % (ctx.path.name),
                      output_node.ant_glob('**/*', quiet = True),
                      cwd = output_node,
                      relative_trick = True,
                      quiet = True)

def cmd_build(ctx, conf_dir = ".", source_dir = "."):
    srcnode = ctx.srcnode.abspath()

    if ctx.env.BUILD_PDF == 'yes':
        doc_pdf(ctx, source_dir, conf_dir)

    if ctx.env.BUILD_SINGLEHTML == 'yes':
        doc_singlehtml(ctx, source_dir, conf_dir)

    doc_html(ctx, source_dir, conf_dir)

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
                   action='store_true',
                   default = False,
                   help = "Build PDF.")
    ctx.add_option('--singlehtml',
                   action='store_true',
                   default = False,
                   help = "Build Single HTML file, requires Node Inliner")

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
        sys.path.insert(0, top_dir.find_node(doc).abspath())
        #
        # Import using the imp API so the module is reloaded for us.
        #
        import imp
        mf = imp.find_module('conf')
        try:
            bconf = imp.load_module('bconf', mf[0], mf[1], mf[2])
        finally:
            mf[0].close()
        sys.path = sp[:]
        catalogue[doc] = {
            'title': bconf.project,
            'version':  bconf.version,
            'release': bconf.release,
            'pdf': bconf.latex_documents[0][1].replace('.tex', '.pdf'),
            'html': '%s/index.html' % (doc),
            'singlehtml': '%s.html' % (doc)
        }
        bconf = None

    import xml.dom.minidom as xml
    cat = xml.Document()

    root = cat.createElement('rtems-docs')
    root.setAttribute('date', 'today')
    cat.appendChild(root)

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

CONF_FRAG = """
sys.path.append(os.path.abspath('../../common/'))
sys.path.append('%s')
templates_path = ['_templates']
html_static_path = ['_static']
"""

# XXX: fix this ugly hack.  No time to waste on it.
def cmd_build_path(ctx):
    def run(task):

        with open("conf.py") as fp:
            conf = "import sys, os\nsys.path.append(os.path.abspath('../../common/'))\n"
            conf += fp.read()

        task.inputs[0].abspath()
        task.outputs[0].write(conf + (CONF_FRAG % ctx.env.RTEMS_PATH))

    ctx(
        rule   = run,
        source = [ctx.path.parent.find_node("common/conf.py"),
                  ctx.path.find_node("./conf.py")],
        target = ctx.path.get_bld().make_node('conf.py')
    )

    cmd_build(ctx, conf_dir = "build", source_dir = "build")
