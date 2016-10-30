import sys, os, re
from waflib.Build import BuildContext

sphinx_min_version = (1,3)


def cmd_spell(ctx):
	from waflib import Options
	from sys import argv
	from subprocess import call

	Options.commands = None # stop warnings about knowing commands.

	if not ctx.env.BIN_ASPELL:
		ctx.fatal("'aspell' is required please add binary to your path and re-run configure.")

	if len(argv) < 3:
		ctx.fatal("Please supply at least one file name")

	files = argv[2:]

	path = ctx.path.parent.abspath()

	# XXX: add error checking eg check if file exists.
	for file in files:
		cmd = ctx.env.BIN_ASPELL + ["-c", "--personal=%s/common/spell/dict/rtems" % path, "--extra-dicts=%s/common/spell/en_GB-ise-w_accents.multi" % path, file]

		print("running:", cmd)
		call(cmd)


def cmd_linkcheck(ctx, conf_dir=".", source_dir="."):
	ctx(
		rule	= "${BIN_SPHINX_BUILD} -b linkcheck -c %s -j %d -d build/doctrees %s build/linkcheck" % (conf_dir, ctx.options.jobs, source_dir),
		cwd		= ctx.path.abspath(),
		source	= ctx.path.ant_glob('**/*.rst'),
		target	= "linkcheck/output.txt"
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
	version = ctx.cmd_and_log(ctx.env.BIN_SPHINX_BUILD + ['--version']).split(" ")[-1:][0].strip()
	try:
		ver = tuple(map(int, re.split('[\D]', version)))
	except:
		ctx.fatal("Sphinx version cannot be checked: %s" % version)
	if ver < minver:
		ctx.fatal("Sphinx version is too old: %s" % ".".join(map(str, ver)))

	return ver

def sphinx_verbose(ctx):
        return ctx.options.sphinx_verbose

def cmd_configure(ctx):
	ctx.load('tex')

	ctx.env.append_value('PDFLATEXFLAGS', '-shell-escape')

	ctx.find_program("sphinx-build", var="BIN_SPHINX_BUILD", mandatory=True)
	ctx.find_program("aspell", var="BIN_ASPELL", mandatory=False)
	ctx.find_program("inliner", var="BIN_INLINER", mandatory=False)

	ctx.start_msg("Checking if Sphinx is at least %s.%s" % sphinx_min_version)
	ver = check_sphinx_version(ctx, sphinx_min_version)

	ctx.end_msg("yes (%s)" % ".".join(map(str, ver)))


def html_resources(ctx):
	for dir_name in ["_static", "_templates"]:
		files = ctx.path.parent.find_node("common").ant_glob("%s/*" % dir_name)
                fnode = ctx.path.get_bld().make_node(os.path.join('html', dir_name))
		fnode.mkdir() # dirs
		ctx(
			features = "subst",
			is_copy  = True,
			source   = files,
			target   = [fnode.make_node(x.name) for x in files]
		)

	# copy images
#	ctx.path.get_bld().make_node("images").mkdir()
#	files = ctx.path.parent.ant_glob("images/**")
#	ctx(
#		features    = "subst",
#		is_copy     = True,
#		source      = files,
#		target      = [x.srcpath().replace("../", "") for x in files]
#	)

def doc_pdf(ctx, source_dir, conf_dir):
	if not ctx.env.PDFLATEX or not ctx.env.MAKEINDEX:
		ctx.fatal('The programs pdflatex and makeindex are required')

        build_dir = ctx.path.get_bld().relpath()
        output_node = ctx.path.get_bld().make_node('latex')
        output_dir = output_node.abspath()

	ctx(
		rule         = "${BIN_SPHINX_BUILD} %s -b latex -c %s -d build/%s/doctrees %s %s" % (sphinx_verbose(ctx), conf_dir, build_dir, source_dir, output_dir),
		cwd          = ctx.path,
		source       = ctx.path.ant_glob('**/*.rst'),
		target       = ctx.path.find_or_declare("latex/%s.tex" % (ctx.path.name))
	)

	ctx.add_group()

	ctx(
		features     = 'tex',
		cwd          = output_dir,
		type         = 'pdflatex',
		source       = "latex/%s.tex" % ctx.path.name,
		prompt       = 0
	)

        ctx.install_files('${PREFIX}/%s' % (ctx.path.name),
                          'latex/%s.pdf' % (ctx.path.name),
                          cwd = output_node,
                          quiet = True)

def doc_singlehtml(ctx, source_dir, conf_dir):
	if not ctx.env.BIN_INLINER:
		ctx.fatal("Node inliner is required install with 'npm install -g inliner' (https://github.com/remy/inliner)")

	html_resources(ctx)

	ctx(
		rule	= "${BIN_SPHINX_BUILD} -b singlehtml -c %s -j %d -d build/doctrees %s build/singlehtml" % (conf_dir, ctx.options.jobs, source_dir),
		cwd		= ctx.path.abspath(),
		source	= ctx.path.ant_glob('**/*.rst'),
		target	= "singlehtml/index.html",
                install_path = None
	)

	ctx.add_group()

	ctx(
		rule	= "${BIN_INLINER} ${SRC} > ${TGT}",
		source	= "singlehtml/index.html",
		target	= "singlehtml/%s.html" % ctx.path.name,
                install_path = None
	)

def doc_html(ctx, conf_dir, source_dir):

	html_resources(ctx)

        build_dir = ctx.path.get_bld().relpath()
        output_node = ctx.path.get_bld().make_node('html')
        output_dir = output_node.abspath()

	ctx(
		rule         = "${BIN_SPHINX_BUILD} %s -b html -c %s -d build/%s/doctrees %s %s" % (sphinx_verbose(ctx), conf_dir, build_dir, source_dir, output_dir),
		cwd          = ctx.path,
		source       =  ctx.path.ant_glob('**/*.rst'),# + ctx.path.ant_glob('conf.py'),
		target       = ctx.path.find_or_declare('html/index.html'),
		install_path = None
	)

        ctx.install_files('${PREFIX}/%s' % (ctx.path.name),
                          output_node.ant_glob('**/*'),
                          cwd = output_node,
                          relative_trick = True,
                          quiet = True)

def is_top_build(ctx):
        from_top = False
        if ctx.env['BUILD_FROM_TOP'] and ctx.env['BUILD_FROM_TOP'] == 'yes':
                from_top = True
        return from_top

def build_type(ctx):
        build_type = 'html'
        if ctx.options.pdf:
                build_type = 'pdf'
        return build_type

def build_dir_setup(ctx):
        btype = build_type(ctx)
        where = btype
        if is_top_build(ctx):
                where = os.path.join(ctx.path.name, where)
        bnode = ctx.bldnode.find_node(where)
        if bnode is None:
                ctx.bldnode.make_node(where).mkdir()
        return where

def cmd_build(ctx, conf_dir = ".", source_dir = "."):
        build_dir_setup(ctx)

	srcnode = ctx.srcnode.abspath()

	if ctx.options.pdf:
		doc_pdf(ctx, source_dir, conf_dir)
	elif ctx.options.singlehtml:
		html_resources(ctx)
		doc_singlehtml(ctx, source_dir, conf_dir)
	else:
		doc_html(ctx, source_dir, conf_dir)

def cmd_options(ctx):
	ctx.add_option('--sphinx-verbose', action='store', default="-Q", help="Sphinx verbose.")
	ctx.add_option('--pdf', action='store_true', default=False, help="Build PDF.")
	ctx.add_option('--singlehtml', action='store_true', default=False, help="Build Single HTML file, requires Node Inliner")


def cmd_options_path(ctx):
	cmd_options(ctx)
	ctx.add_option('--rtems-path-py', type='string', help="Full path to py/ in RTEMS source repository.")


def cmd_configure_path(ctx):
	if not ctx.options.rtems_path_py:
		ctx.fatal("--rtems-path-py is required")

	ctx.env.RTEMS_PATH = ctx.options.rtems_path_py

	cmd_configure(ctx)


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
		source = [ctx.path.parent.find_node("common/conf.py"), ctx.path.find_node("./conf.py")],
		target = ctx.path.get_bld().make_node('conf.py')
    )

	cmd_build(ctx, conf_dir="build", source_dir="build")
