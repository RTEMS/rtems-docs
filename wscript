#
# RTEMS Project Documentation
#

from sys import path
from os.path import abspath
path.append(abspath('common'))

import waflib
import waf as docs_waf

version = 'Master (4.11.99)'

build_all = ['user',
             'rsb',
             'c-user',
             'bsp-howto',
             'posix-users',
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
    docs_waf.xml_catalogue(ctx, building, version)

def build(ctx):
    for b in building:
        ctx.recurse(b)
    ctx(rule = catalogue,
        target = 'catalogue.xml',
        source = ['wscript', 'common/waf.py'])
    ctx.install_files('${PREFIX}', 'catalogue.xml')

def install(ctx):
    for b in building:
        ctx.recurse(b)
