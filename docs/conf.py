#
from os import environ, path

import sys

sys.path.insert(0, path.abspath(".."))

# Package
from gml_application_schema_toolbox import __about__

# -- Build environment -----------------------------------------------------
on_rtd = environ.get("READTHEDOCS", None) == "True"

# -- Project information -----------------------------------------------------
project = __about__.__title__
author = __about__.__author__
copyright = __about__.__copyright__
version = release = __about__.__version__
github_doc_root = "{}/tree/master/doc/".format(__about__.__uri_repository__)

myst_substitutions = {
    "title": project,
    "author": author,
    "repo_url": __about__.__uri__,
    "version": version,
}

myst_url_schemes = ("http", "https", "mailto")

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Sphinx included
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
    # 3rd party
    "myst_parser",
]


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {".md": "markdown"}
autosectionlabel_prefix_document = True
# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", ".venv", "Thumbs.db", ".DS_Store", "_output", "ext_libs"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# -- Theme

html_favicon = (
    "../gml_application_schema_toolbox/resources/gml_application_schema_toolbox.png"
)
html_logo = (
    "../gml_application_schema_toolbox/resources/gml_application_schema_toolbox.png"
)
html_static_path = ["static"]
html_theme = "furo"
# html_theme_options = {
#     "github_url": __about__.__uri_repository__,
#     "repository_url": __about__.__uri_repository__,
# }


myst_enable_extensions = [
    "deflist",
    "html_image",
    "smartquotes",
    "replacements",
    "linkify",
    "substitution",
]
# -- EXTENSIONS --------------------------------------------------------

# Configuration for intersphinx (refer to others docs).
intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}