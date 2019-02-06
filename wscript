#
# RTEMS Project Documentation
#

import sys
import os.path

sys.path.append(os.path.abspath('common'))

import waflib
import waf as docs_waf
import version

#
# Branch version
#
rtems_major_version = '5'

#
# The documents to build.
#
build_all = ['user',
             'c-user',
             'bsp-howto',
             'posix-users',
             'posix-compliance',
             'eng',
             'filesystem',
             'networking',
             'shell',
             'cpu-supplement',
             'develenv',
             'eclipse']

building = build_all

def options(opt):
    docs_waf.cmd_options(opt)

def configure(conf):
    for b in building:
        conf.recurse(b)
    conf.env['BUILD_FROM_TOP'] = 'yes'

def catalogue(ctx):
    docs_waf.xml_catalogue(ctx, building)

def coverpage_js(ctx):
    js = None
    xml = None
    for f in ctx.inputs:
        if f.abspath().endswith('.js'):
            with open(f.abspath()) as i:
                js = i.read()
        elif f.abspath().endswith('.xml'):
            with open(f.abspath()) as i:
                xml = i.read()
    xml = xml.replace('\n', ' \\\n');
    with open(ctx.outputs[0].abspath(), 'w') as o:
        o.write(js.replace('@CATALOGUE', xml))


def build(ctx):
    #
    # Get the version.
    #
    ver_version, ver_date = version.get(ctx, rtems_major_version)
    ctx.env.DATE = ver_date
    ctx.env.RELEASE = ver_version + ' (' + ver_date + ')'
    ctx.env.VERSION = ver_version
    ctx.to_log('Build: %s%s' % (ctx.env.RELEASE, os.linesep))

    #
    #
    # Generate any PlantUML images if enabled.
    #
    ctx.recurse('images')
    ctx.add_group('images')

    for b in building:
        ctx.recurse(b)

    #
    # Build the catalogue, coverpage.js and install.
    #
    ctx(rule = catalogue,
        target = 'catalogue.xml',
        source = ['wscript', 'common/waf.py'] + ['%s/conf.py' % x for x in building])
    ctx.install_files('${PREFIX}', 'catalogue.xml')
    ctx(rule = coverpage_js,
        target = 'coverpage.js',
        source = ['wscript', 'catalogue.xml', 'common/coverpage/coverpage.js'])
    ctx.install_as('${PREFIX}/coverpage.js', 'coverpage.js')
    #
    # Install the static content.
    #
    ctx.install_as('${PREFIX}/index.html', 'common/coverpage/coverpage.html')
    static_dir = ctx.path.find_dir('common/coverpage/static')
    ctx.install_files('${PREFIX}/static',
                      static_dir.ant_glob('**'),
                      cwd = static_dir,
                      relative_trick = True)

def install(ctx):
    for b in building:
        ctx.recurse(b)

def cmd_spell(ctx):
    for b in building:
        ctx.recurse(b)

def cmd_linkcheck(ctx):
    for b in building:
        ctx.recurse(b)
