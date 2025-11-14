
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "HPR-LP"
html_title = "HPR-LP"
html_short_title = "HPR-LP"


copyright = '2025, HPR Methods Developer Team'
author = 'HPR  Methods Developer Team' 

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc", "sphinx.ext.autosummary",
    "sphinx.ext.napoleon", "sphinx.ext.viewcode",
    "sphinx.ext.mathjax", "sphinxcontrib.pseudocode",
]
autosummary_generate = True
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_permalinks = False

# extensions = ["myst_parser", "sphinx.ext.mathjax"]
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]
mathjax3_config = {
    "tex": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
    }
}


source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# -- Options for HTML output -------------------------------------------------

html_favicon = "../assets/favicon.ico"


# html_theme = "furo"
# html_theme = "sphinx_book_theme"
# html_theme = "pydata_sphinx_theme"
html_theme = "renku" #  like OSQP
#html_theme = "press"


html_show_sourcelink = False

html_static_path = ["_static"]
html_js_files = ['back_to_hpr_fab.js']
html_css_files = [
    "custom.css",
]

html_theme_options = { 
    "collapse_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "sticky_navigation": True,
    # "titles_only": False,
}

