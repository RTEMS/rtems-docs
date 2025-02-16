#
# RTEMS Project Documentation
#

import sys
import os.path

import waflib

#
# Set Python's system path to `common` from the top level so the
# conf.py modules in subdirectories can be found. See xml_catalogue in
# common/waf.py.
#
sys.path.append(os.path.abspath('common'))

from common import waf as docs_waf
from common import version

#
# Branch version
#
rtems_major_version = '7'

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
             'shell',
             'cpu-supplement',
             'develenv']

building = build_all

def options(opt):
    docs_waf.cmd_options(opt)

def configure(conf):
    conf.find_program('git')
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

def index_html(ctx):
    html = ''
    year = ctx.env.DATE.split()[2]
    for f in ctx.inputs:
        if f.abspath().endswith('.html'):
            with open(f.abspath()) as i:
                html += i.read()
    with open(ctx.outputs[0].abspath(), 'w') as o:
        html = html.replace('@COPYRIGHT_YEAR@', year)
        html = html.replace('@VER_DATE@', ctx.env.DATE)
        o.write(html)

def build(ctx):
    #
    # Get the version.
    #
    ver_version, ver_date, ver_released = version.get(ctx, rtems_major_version)
    ctx.env.DATE = ver_date
    ctx.env.RELEASE = ver_version + ' (' + ver_date + ')'
    ctx.env.VERSION = ver_version
    ctx.env.RTEMS_MAJOR = version.major()
    ctx.env.RTEMS_MINOR = version.minor()
    ctx.env.RTEMS_REVISION = version.revision()
    ctx.env.RTEMS_RELEASED = version.released()
    ctx.to_log('Build: %s%s' % (ctx.env.RELEASE, os.linesep))

    #
    #
    # Generate any PlantUML images if enabled.
    #
    ctx.recurse('images')
    ctx.add_group('images')

    if ctx.env.DOC_LIST:
        global building
        for doc in ctx.env.DOC_LIST:
            if doc not in building:
                ctx.fatal("'{}' not in doc list".format(doc))
        building = ctx.env.DOC_LIST

    for b in building:
        ctx.recurse(b)

    #
    # Build the catalogue, coverpage.js, index.html and install.
    #
    ctx(rule = catalogue,
        target = 'catalogue.xml',
        source = ['wscript', 'common/waf.py'] + ['%s/conf.py' % x for x in building])
    ctx.install_files('${PREFIX}', 'catalogue.xml')
    ctx(rule = coverpage_js,
        target = 'coverpage.js',
        source = ['wscript', 'catalogue.xml', 'common/coverpage/coverpage.js'])
    ctx.install_as('${PREFIX}/coverpage.js', 'coverpage.js')
    ctx(rule = index_html,
        target = 'coverpage.html',
        source = ['wscript', 'common/coverpage/coverpage.html'])
    ctx.install_as('${PREFIX}/index.html', 'coverpage.html')
    #
    # Install the static content.
    #
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
