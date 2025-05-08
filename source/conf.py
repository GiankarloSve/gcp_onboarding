# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'gcp_onboarding'
copyright = '2025, A.Sverko & G.Sverko'
author = 'A.Sverko & G.Sverko'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
     'myst_parser',
     'sphinx_copybutton',
     'sphinxcontrib.plantuml',
     'sphinxcontrib.spelling',
]

# Running the Spell Checker:
# To check spelling in your documentation, use the following command in terminal when in the proper directory for your sphinx project:
# sphinx-build -b spelling source/ build/spelling

# Language for spell checker extension
spelling_lang = 'en_US'

# Support both .rst and .md source files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_options = {
    "navigation_with_keys": True,
}


html_static_path = ['_static']
