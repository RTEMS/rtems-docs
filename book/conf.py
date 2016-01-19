import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '1.0'
release = '5.0'

latex_documents = [
	('index', 'book.tex', u'RTEMS Book', u'RTEMS Documentation Project', 'manual'),
]

