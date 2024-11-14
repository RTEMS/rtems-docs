import datetime

# General information about the project.
project = u'RTEMS Documentation Project'
copyright = u'1988-'+ str(datetime.datetime.now().year) + ' RTEMS Project and contributors'
author = "RTEMS Project"
#doc_source_path = "SET_ON_COMMANDLINE"

# The master toctree document.
master_doc = 'index'

extensions = [
	"sphinx.ext.autodoc",
	"sphinx.ext.coverage",
	"sphinx.ext.doctest",
	"sphinx.ext.extlinks",
	"sphinx.ext.graphviz",
	"sphinx.ext.intersphinx",
	"sphinx.ext.mathjax",
	"sphinxcontrib.bibtex",
	"sphinxcontrib.jquery",
	"rtemsdomain",
	"sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'http://docs.python.org/': None}

# http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-numfig
numfig = True


html_theme = "sphinx_book_theme"
html_logo = "../common/_static/logo.webp"
html_favicon = "../common/_static/favicon_docs.ico"
#html_title = "*REPLACE* SET ON THE COMMANDLINE *REPLACE*"
html_copy_source = True
html_last_updated_fmt = ""
html_static_path = ['../common/_static']
html_css_files = ['custom.css',]

html_context = {
    "gitlab_url": "https://gitlab.rtems.org",
    "gitlab_user": "rtems/docs",
    "gitlab_repo": "rtems-docs",
    "gitlab_version": "main",
    "doc_path": "SET_ON_COMMANDLINE",
}


html_theme_logo = {
    "text": "SET_ON_COMMANDLINE"
}

html_theme_version_switcher = {
        "json_url": "https://docs.rtems.org/docs_version_switcher.json",
        "version_match": "SET_ON_COMMANDLINE",
}

html_theme_options = {
    "use_sidenotes": True,
    "repsitory_provider": "gitlab",
    "use_source_button": True,
    "use_edit_page_button": True,
    "use_repository_button": True,
    "use_issues_button": True,
    "show_toc_level": 4,
    "use_fullscreen_button": True,
    "use_repository_button": True,
    "logo": html_theme_logo,
    "switcher": html_theme_version_switcher
}

html_sidebars = {
    "**": ["navbar-logo.html","icon-links.html", "version-switcher", "search-button-field.html","sbt-sidebar-nav.html"]

}



bibtex_bibfiles = ['../common/refs.bib']
extlinks = {'release_path': ('https://ftp.rtems.org/pub/rtems/releases', None) }
# The suffix of source filenames.
source_suffix = '.rst'


pygments_style = 'default' # sphinx
htmlhelp_basename = 'rtemsdoc'


# -- Options for LaTeX output --------------------------------------------------
latex_engine = 'pdflatex'

latex_use_xindy = False

latex_paper_size = 'a4'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [] # must be overridden in local conf.py

# Additional stuff for LaTeX
#    'fontpkg':      r'\usepackage{mathpazo}',
latex_elements = {
    'papersize':    'a4paper',
    'pointsize':    '11pt',
    'releasename':  '',
    'preamble':     r'''
\newcommand{\rtemscopyright}{%s}
\usepackage{rtemsstyle}
''' % (copyright),
    'maketitle': r'\rtemsmaketitle',
    'parsedliteralwraps': True,
}

latex_additional_files = ['../common/rtemsstyle.sty', '../common/logo.pdf']
latex_use_modindex = False

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
#latex_show_urls=True

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

highlight_language = "c"
