import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

version = '1.0'
release = '5.0'

latex_documents = [
	('index', 'book.tex', u'RTEMS Book', u'RTEMS Documentation Project', 'manual'),
]

