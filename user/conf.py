import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.0'
release = '4.11.0'

project = "RTEMS User Manual"

exclude_patterns = ['config/build.rst',
                    'config/runtime.rst',
                    'start/depend.rst',
                    'start/transition.rst',
                    'start/releases.rst',
                    'start/development.rst',
                    'start/installation.rst',
                    'start/windows.rst',
                    'test/create.rst',
                    'test/running.rst',
                    'tools/build.rst',
                    'tools/simulation.rst',
                    'waf/index.rst']

latex_documents = [
	('index', 'user.tex', u'RTEMS User Manual', u'RTEMS Documentation Project', 'manual'),
]
