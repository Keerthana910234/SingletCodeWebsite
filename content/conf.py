#Adapted from the sphinx-tutorial and https://github.com/tomography/tomobank/blob/master and https://github.com/coderefinery/documentation/blob/main/content/conf.py

# Configuration file for the Sphinx documentation builder.
# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.


import sphinx_rtd_theme
import os, sys

# We require sphinx >=2 because of sphinxcontrib.bibtex,
needs_sphinx = '2.0'

# -- Project information -----------------------------------------------------
# General information about the project.
Affiliation = u'Goyal Lab'
project = u'SingletCode'
copyright = u'2023, ' + Affiliation
github_repo_name = "SingletCodeWebsite"
github_version = "main"
# The full version, including alpha/beta/rc tags
currentVersion = open("../VERSION").read().strip()
release = currentVersion
conf_py_path = "/content/" # with leading and trailing slash


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.githubpages',
    'sphinxcontrib.bibtex',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_rtd_size',
    "sphinx_rtd_theme_ext_color_contrast",
]
sphinx_rtd_size_width = "90%"

bibtex_bibfiles = [
    'bibtex/ref.bib'
]
nb_execution_mode = "cache"

todo_include_todos=True


# The suffix of source filenames.
source_suffix = '.md'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "README*",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
    "*venv*",
]
show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


from os.path import basename, dirname, realpath

html_context = {
    "display_github": False,
    # Auto-detect directory name.  This can break, but
    # useful as a default.
    "github_repo": github_repo_name or basename(dirname(realpath(__file__))),
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}

import os
if os.environ.get('GITHUB_REF', '') == 'refs/heads/'+github_version:
    html_js_files = [
        ('https://plausible.cs.aalto.fi/js/script.js', {"data-domain": "coderefinery.github.io", "defer": "defer"}),
    ]


bibtex_bibfiles = [
    'bibtex/ref.bib',
    ]

