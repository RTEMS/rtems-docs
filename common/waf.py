import sys, os



def cmd_configure(ctx):
	ctx.find_program("sphinx-build", var="SPHINX_BUILD")

def cmd_build(ctx, conf_dir=".", source_dir="."):
	srcnode = ctx.srcnode.abspath()

	# Copy resources.
	for dir in ["_static", "_templates"]:
		files = ctx.path.parent.find_node("common").ant_glob("%s/*" % dir)
		ctx.path.get_bld().make_node(dir).mkdir() # dirs

		ctx(
			features    = "subst",
			is_copy     = True,
			source      = files,
			target      = [ctx.bldnode.find_node(dir).get_bld().make_node(x.name) for x in files]
		)

	ctx(
		rule   = "${SPHINX_BUILD} -b html -c %s -j %d -d build/doctrees %s build/html" % (conf_dir, ctx.options.jobs, source_dir),
		cwd	= ctx.path.abspath(),
		source =  ctx.path.ant_glob('**/*.rst'),# + ctx.path.ant_glob('conf.py'),
		target = ctx.path.find_or_declare('html/index.html')
	)

def cmd_options_path(ctx):
	ctx.add_option('--rtems-path-py', type='string', help="Path to py/ in RTEMS.")


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
