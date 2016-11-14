#
# RTEMS Project Documentation
#

from sys import path
from os.path import abspath
path.append(abspath('common'))

import waf as docs_waf

build_all = ['bsp-howto',
             'c-user',
             'cpu-supplement',
             'develenv',
             'eclipse',
             'filesystem',
             'networking',
             'posix-users',
             'rsb',
             'shell',
             'user']

building = build_all

def options(opt):
    docs_waf.cmd_options(opt)

def configure(conf):
    for b in building:
        conf.recurse(b)
    conf.env['BUILD_FROM_TOP'] = 'yes'

def build(ctx):
    for b in building:
        ctx.recurse(b)

def install(ctx):
    for b in building:
        ctx.recurse(b)
