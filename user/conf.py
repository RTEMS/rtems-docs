import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.0'
release = '4.11.0'

project = "RTEMS User Manual"

exclude_patterns = ['config/build.rst',
                    'config/runtime.rst',

                    'start/installation.rst',
                    'start/basics.rst',
                    'start/depend.rst',
                    'start/quick.rst',

                    'start/transition.rst',

                    'hosts/os.rst',
                    'hosts/prefixes.rst',
                    'hosts/macos.rst',
                    'hosts/posix.rst',
                    'hosts/windows.rst',

                    'installation/prefixes-sandboxing.rst',
                    'installation/releases.rst',
                    'installation/developer.rst',

                    'tools/build.rst',
                    'tools/simulation.rst',

                    'test/create.rst',
                    'test/running.rst',

                    'waf/index.rst']

latex_documents = [
	('index', 'user.tex', u'RTEMS User Manual', u'RTEMS Documentation Project', 'manual'),
]
