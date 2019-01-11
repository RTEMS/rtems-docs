#
# RTEMS Project Documentation
#

from sys import path
from os.path import abspath
path.append(abspath('common'))

import waflib
import waf as docs_waf

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

def pretty_day(day):
    if day == 3:
        s = 'rd'
    elif day == 11:
        s = 'th'
    elif day == 12:
        s = 'th'
    elif day == 13:
        s = 'th'
    elif day % 10 == 1:
        s = 'st'
    elif day % 10 == 2:
        s = 'nd'
    else:
        s = 'th'
    return str(day) + s

def build(ctx):
    #
    # Get date and version from Git
    #
    version = '5.0.0'
    if ctx.exec_command(['git', 'diff-index', '--quiet', 'HEAD']) == 0:
        modified = ''
    else:
        modified = '-modified'
    try:
        out = ctx.cmd_and_log(['git', 'log', '-1', '--format=%H,%cd', '--date=format:%e,%B,%Y'])
        f = out.strip('\n').split(',')
        version = version + '.' + f[0] + modified
        date = pretty_day(int(f[1])) + ' ' + f[2] + ' ' + f[3]
    except waflib.Build.Errors.WafError:
        date = 'unknown date'
    ctx.env.DATE = date
    ctx.env.RELEASE = version + ' (' + date + ')'
    ctx.env.VERSION = version

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
