import sys, os
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

		print "running:", cmd
		call(cmd)


class spell(BuildContext):
	__doc__ = "Check spelling.  Supply a list of files or a glob (*.rst)"
	cmd = 'spell'
	fun = 'cmd_spell'


def check_sphinx_version(ctx, minver):
	version = ctx.cmd_and_log(ctx.env.BIN_SPHINX_BUILD + ['--version']).split(" ")[-1:][0]
	ver = tuple(map(int, version.split(".")))

	if ver < minver:
		ctx.fatal("Sphinx version is too old: %s" % ".".join(map(str, ver)))

	return ver


def cmd_configure(ctx):
	ctx.load('tex')

	ctx.find_program("sphinx-build", var="BIN_SPHINX_BUILD", mandatory=True)
	ctx.find_program("aspell", var="BIN_ASPELL", mandatory=False)
	ctx.find_program("inliner", var="BIN_INLINER", mandatory=False)

	ctx.start_msg("Checking if Sphinx is at least %s.%s" % sphinx_min_version)
	ver = check_sphinx_version(ctx, sphinx_min_version)

	ctx.end_msg("yes (%s)" % ".".join(map(str, ver)))


def doc_pdf(ctx, source_dir, conf_dir):
	if not ctx.env.PDFLATEX or not ctx.env.MAKEINDEX:
		ctx.fatal('The programs pdflatex and makeindex are required')

	ctx(
		rule	= "${BIN_SPHINX_BUILD} -b latex -c %s -j %d -d build/doctrees %s build/latex" % (conf_dir, ctx.options.jobs, source_dir),
		cwd		= ctx.path.abspath(),
		source	= ctx.path.ant_glob('**/*.rst'),
		target	= "latex/%s.tex" % ctx.path.name
	)

	ctx.add_group()

	ctx(
		features	= 'tex',
		cwd			= "%s/latex/" % ctx.path.get_bld().abspath(),
		type		= 'pdflatex',
		source		= ctx.bldnode.find_or_declare("latex/%s.tex" % ctx.path.name),
		prompt		= 0
	)


def doc_singlehtml(ctx, source_dir, conf_dir):
	if not ctx.env.BIN_INLINER:
		ctx.fatal("Node inliner is required install with 'npm install -g inliner' (https://github.com/remy/inliner)")

	ctx(
		rule	= "${BIN_SPHINX_BUILD} -b singlehtml -c %s -j %d -d build/doctrees %s build/singlehtml" % (conf_dir, ctx.options.jobs, source_dir),
		cwd		= ctx.path.abspath(),
		source	= ctx.path.ant_glob('**/*.rst'),
		target	= "singlehtml/index.html"
	)

	ctx.add_group()

	ctx(
		rule	= "${BIN_INLINER} ${SRC} > ${TGT}",
		source	= "singlehtml/index.html",
		target	= "singlehtml/%s.html" % ctx.path.name
	)


def html_resources(ctx):
	for dir in ["_static", "_templates"]:
		files = ctx.path.parent.find_node("common").ant_glob("%s/*" % dir)
		ctx.path.get_bld().make_node(dir).mkdir() # dirs

		ctx(
			features    = "subst",
			is_copy     = True,
			source      = files,
			target      = [ctx.bldnode.find_node(dir).get_bld().make_node(x.name) for x in files]
		)


def cmd_build(ctx, conf_dir=".", source_dir="."):
	srcnode = ctx.srcnode.abspath()

	if not ctx.env.PDFLATEX or not ctx.env.MAKEINDEX:
		ctx.fatal('The programs pdflatex and makeindex are required')


	if ctx.options.pdf:
		doc_pdf(ctx, source_dir, conf_dir)
	elif ctx.options.singlehtml:
		html_resources(ctx)
		doc_singlehtml(ctx, source_dir, conf_dir)
	else:
		html_resources(ctx)
		ctx(
			rule   = "${BIN_SPHINX_BUILD} -b html -c %s -j %d -d build/doctrees %s build/html" % (conf_dir, ctx.options.jobs, source_dir),
			cwd	= ctx.path.abspath(),
			source =  ctx.path.ant_glob('**/*.rst'),# + ctx.path.ant_glob('conf.py'),
			target = ctx.path.find_or_declare('html/index.html')
		)

def cmd_options(ctx):
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
