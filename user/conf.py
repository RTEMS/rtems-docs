import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

project = "RTEMS User Manual"

exclude_patterns = ['config/build.rst',
                    'config/runtime.rst',

                    'start/quick.rst',

                    'hosts/os.rst',
                    'hosts/prefixes.rst',
                    'hosts/macos.rst',
                    'hosts/posix.rst',
                    'hosts/windows.rst',

                    'installation/prefixes-sandboxing.rst',
                    'installation/releases.rst',
                    'installation/developer.rst',
                    'installation/kernel.rst',

                    'hardware/targets.rst',
                    'hardware/architectures.rst',
                    'hardware/bsps.rst',
                    'hardware/tiers.rst',

                    'tools/build.rst',
                    'tools/simulation.rst',

                    'test/create.rst',
                    'test/running.rst',
                    'start/installation.rst',
                    'start/transition.rst',

                    'waf/index.rst']

latex_documents = [
    ('index',
     'user.tex',
     u'RTEMS User Manual',
     u'RTEMS Documentation Project',
     'manual'),
]
