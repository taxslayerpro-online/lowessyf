# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'lowes.syf.com/activate – Activation Guide'
copyright = '2026, Activation Guide'
author = 'Activation Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

# Allow raw HTML inside .rst files
raw_enabled = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# html_theme = 'sphinx_rtd_theme'

# SEO-optimized titles
html_title = "lowes.syf.com/activate – Official Activation Guide 2026"
html_short_title = "lowes.syf.com/activate"

# Favicon (place in _static folder)
html_favicon = 'favicon.ico'

# Hide source link
html_show_sourcelink = False

# Allow unsafe raw HTML (for buttons, banners, CTAs)
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static files
# html_static_path = ['_static']
