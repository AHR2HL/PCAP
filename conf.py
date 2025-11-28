# -*- coding: utf-8 -*-
#
# PCAP Python Certification Preparation Course
# Configuration file for Sphinx documentation builder
#

import sys, os
from runestone import runestone_static_dirs, runestone_extensions, setup
import pkg_resources

# -- General configuration -----------------------------------------------------

extensions = ["sphinx.ext.mathjax", "jupyterlite_sphinx"] + runestone_extensions()

templates_path = [
    pkg_resources.resource_filename("runestone", "common/project_template/_templates")
]

source_suffix = ".rst"
master_doc = "index"

# -- Project information -------------------------------------------------------

project = "Python Advanced Certification (PCAP)"
copyright = "2024, Alpha Schools"

course_description = """Advanced preparation course for the PCAP-31-03 Python Associate Programmer Certification. Covers object-oriented programming, inheritance, exceptions, advanced functions including closures and decorators, file I/O operations, and professional Python programming techniques required for the PCAP certification exam."""

key_words = "python certification pcap exam preparation associate programmer oop classes inheritance exceptions decorators advanced"
shelf_section = "Level 2. Advanced Computer Science"

generate_component_labels = False

# Version info
version = "1.0"
release = "1.0.0"

# Language
language = "en"

# Build configuration
exclude_patterns = []
pygments_style = "sphinx"
keep_warnings = True

rst_prolog = (
    """

.. |blank| replace:: :blank:`x`
"""
)

# -- HTML output options -------------------------------------------------------

html_theme = "sphinx_bootstrap"

html_theme_options = {
    "navbar_title": "PCAP Certification Prep",
    "navbar_site_name": "Chapters",
    "globaltoc_depth": 1,
    "globaltoc_includehidden": "true",
    "navbar_class": "navbar",
    "navbar_fixed_top": "true",
    "source_link_position": "nav",
}

html_theme_path = [
    pkg_resources.resource_filename(
        "runestone", "common/project_template/_templates/plugin_layouts"
    )
]

html_title = "Python Advanced Certification (PCAP) Prep"
html_short_title = "PCAP Certification"

html_static_path = ["_static", "_sources/_static"] + runestone_static_dirs()

html_show_sourcelink = False
htmlhelp_basename = "PCAPCertificationPrepdoc"