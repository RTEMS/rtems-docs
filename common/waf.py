import sys, os

def cmd_configure(ctx):
	ctx.find_program("sphinx-build", var="SPHINX_BUILD")

def cmd_build(ctx, sub, source_dir="."):
	srcnode = ctx.srcnode.abspath()

	file_conf = ctx.path.parent.find_node("common/conf.py")
	tg = ctx(
		features    = "subst",
		source      = file_conf,
		target		= file_conf.name
	)

	tg.__dict__.update(sub)


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
		rule   = "${SPHINX_BUILD} -b html -c build -j %s -d build/doctrees %s build/html" % (ctx.options.jobs, source_dir),
		cwd	= ctx.path.abspath(),
		source =  ctx.path.ant_glob('**/*.rst') + ctx.path.ant_glob('conf.py'),
		target = ctx.path.find_or_declare('html/index.html')
	)

