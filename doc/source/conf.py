from datetime import datetime
from glob import glob
import os
import sys
from pathlib import Path
import subprocess

from ansys_sphinx_theme import (
    ansys_favicon,
    get_version_match,
    pyansys_logo_dark_mode,
    pyansys_logo_light_mode,
)
import numpy as np
import pyvista

from ansys.dpf.core import __version__, server, server_factory
from ansys.dpf.core.examples import get_example_required_minimum_dpf_version

# Make sphinx_utilities modules importable
sys.path.append(os.path.join(os.path.dirname(__file__), "../sphinx_utilities"))
from version_filtering import get_tutorial_version_requirements

# Manage errors
pyvista.set_error_output_file("errors.txt")
# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True
# Preferred plotting style for documentation
# pyvista.set_plot_theme('document')
pyvista.global_theme.window_size = np.array([1024, 768]) * 2
# Save figures in specified directory
pyvista.FIGURE_PATH = os.path.join(os.path.abspath("./images/"), "auto-generated/")
if not os.path.exists(pyvista.FIGURE_PATH):
    os.makedirs(pyvista.FIGURE_PATH)

pyvista.BUILDING_GALLERY = True

pyvista.global_theme.lighting = False


# -- Project information -----------------------------------------------------

project = "PyDPF-Core"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS Inc."
cname = os.getenv("DOCUMENTATION_CNAME", "dpf.docs.pyansys.com")

# The short X.Y version
version = __version__

# The full version, including alpha/beta/rc tags
release = __version__

# -- Rename files to be ignored with the ignored pattern ---------------------

# Get the DPF server version
server_instance = server.start_local_server(
    as_global=False,
    config=server_factory.AvailableServerConfigs.GrpcServer,
)
server_version = server_instance.version
server.shutdown_all_session_servers()
print("".rjust(40, '*'))
print(f"Doc built for DPF server version {server_version} at:\n{server_instance.ansys_path}")
print("".rjust(40, '*'))

# Build ignore pattern
ignored_pattern = r"(ignore"
for example in sorted(glob(r"../../examples/**/*.py")):
    minimum_version_str = get_example_required_minimum_dpf_version(example)
    if float(server_version) - float(minimum_version_str) < -0.05:
        example_name = example.split(os.path.sep)[-1]
        print(f"Example {example_name} skipped as it requires DPF {minimum_version_str}.")
        ignored_pattern += f"|{example_name}"
ignored_pattern += "|11-server_types.py"
ignored_pattern += "|06-distributed_stress_averaging.py"
ignored_pattern += r")"

exclude_patterns = []
for tutorial_file in glob(str(Path("user_guide")/"tutorials"/"**"/"*.rst")):
    if Path(tutorial_file).name == "index.rst":
        continue
    minimum_version_str = get_tutorial_version_requirements(tutorial_file)
    if float(server_version) - float(minimum_version_str) < -0.05:
        print(f"Tutorial {Path(tutorial_file).name} skipped as it requires DPF {minimum_version_str}.")
        exclude_patterns.append(tutorial_file.replace("\\", "/"))

# Autoapi ignore pattern
autoapi_ignore_list = [
    "*/log.py",
    "*/help.py",
    "*/mapping_types.py",
    "*/ipconfig.py",
    "*/field_base.py",
    "*/cache.py",
    "*/misc.py",
    "*/check_version.py",
    "*/operators/build.py",
    "*/operators/specification.py",
    "*/vtk_helper.py",
    "*/label_space.py",
    "*/examples/python_plugins/*",
    "*/examples/examples.py",
    "*/gate/*",
    "*/gatebin/*",
    "*/grpc/*",
    "*/property_fields_container.py"
]

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "enum_tools.autoenum",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.graphviz",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_jinja",
    'sphinx_reredirects',
    "jupyter_sphinx",
]

redirects = {
     "user_guide/getting_started_with_dpf_server": "../getting_started/dpf_server.html",
     "concepts/index": "../user_guide/index.html#concepts",
     "contributing": "getting_started/contributing.html"
}

typehints_defaults = "comma"
typehints_use_signature = True
simplify_optional_unions = False
autosectionlabel_prefix_document = True
# Intersphinx mapping
intersphinx_mapping = {
    "pyvista": ("https://docs.pyvista.org/", None),
}

autosummary_generate = False

autodoc_mock_imports = ["ansys.dpf.core.examples.python_plugins"]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns.extend(["links_and_refs.rst"])

# make rst_epilog a variable, so you can add other epilog parts to it
rst_epilog = ""

# Read links and targets from file
with open("links_and_refs.rst") as f:
    rst_epilog += f.read()

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Sphinx Gallery Options
sphinx_gallery_conf = {
    # convert rst to md for ipynb
    "pypandoc": True,
    # path to your examples scripts
    "examples_dirs": ["../../examples"],
    # abort build at first example error
    'abort_on_example_error': True,
    # path where to save gallery generated examples
    "gallery_dirs": ["examples"],
    # Pattern to search for example files
    "filename_pattern": r"\.py",
    # Pattern to search for example files to be ignored
    "ignore_pattern": ignored_pattern,
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": "FileNameSortKey",
    # directory where function granular galleries are stored
    "backreferences_dir": None,
    "image_scrapers": ("pyvista", "matplotlib"),
    # 'first_notebook_cell': ("%matplotlib inline\n"
    #                         "from pyvista import set_plot_theme\n"
    #                         "set_plot_theme('document')"),
    "reset_modules_order": 'both',
    "reset_modules": ("reset_servers.reset_servers",),
}


# -- Options for HTML output -------------------------------------------------
html_short_title = html_title = "PyDPF-Core"
html_theme = "ansys_sphinx_theme"
html_favicon = ansys_favicon
html_theme_options = {
    "logo": {
        "image_dark": pyansys_logo_dark_mode,
        "image_light": pyansys_logo_light_mode,
    },
    "logo_link": "https://docs.pyansys.com",
    "github_url": "https://github.com/ansys/pydpf-core",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": get_version_match(__version__),
    },
    "static_search": {
        "threshold": 0.5,
        "limit": 10,
        "minMatchCharLength": 2,
        "ignoreLocation": True,
    },
    "ansys_sphinx_theme_autoapi": {
        "project": project,
        "output": "api",
        "directory": "src/ansys",
        "use_implicit_namespaces": True,
        "keep_files": True,
        "own_page_level": "class",
        "type": "python",
        "options": [
            "inherited-members",
            "members",
            "undoc-members",
            "show-inheritance",
            "show-module-summary",
            "special-members",
        ],
        "class_content": "class",
        "ignore": autoapi_ignore_list,
        "add_toctree_entry": True,
        "member_order": "bysource",
    }
}

# Configuration for Sphinx autoapi
suppress_warnings = [
    "autoapi.python_import_resolution", # TODO: remove suppression of this warning in the future #1967
    "design.grid",
    "config.cache",
    "design.fa-build",
    "autosectionlabel.*",
    "ref.python",
    "toc.not_included"
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'custom.css',
]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_sidebars = {"testing": []}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "pyansysdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "pyansys.tex",
        "PyAnsys DPF-Core Documentation",
        f"{author}",
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "pyansys", "PyAnsys DPF-Core Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "pyansys",
        "PyAnsys DPF-Core Documentation",
        author,
        "pyansys",
        "",
        "Miscellaneous",
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# Define custom docutils roles for solver badges
from sphinx_design.badges_buttons import BadgeRole

def setup(app):
    badge_roles = {
        "bdg-mapdl": "mapdl",
        "bdg-cfx": "cfx",
        "bdg-fluent": "fluent",
        "bdg-lsdyna": "lsdyna"
    }

    for role_name, color in badge_roles.items():
        app.add_role(name=role_name, role=BadgeRole(color=color))

# Common content for every RST file such us links
rst_epilog = ""
links_filepath = Path(__file__).parent.absolute() / "links.rst"
rst_epilog += links_filepath.read_text(encoding="utf-8")

jinja_globals = {
    "PYDPF_CORE_VERSION": version,
}

# Get list of tox environments and add to jinja context
envs = subprocess.run(["tox", "list", "-q"], capture_output=True, text=True).stdout.splitlines()
envs.remove("default environments:")
envs.remove("additional environments:")
envs.remove("")

jinja_contexts = {
    "toxenvs" : {
        "envs": envs,
    }
}

# Optionally exclude api or example documentation generation.
BUILD_API = True if os.environ.get("BUILD_API", "true") == "true" else False
if BUILD_API:
    extensions.extend(["ansys_sphinx_theme.extension.autoapi"])

BUILD_EXAMPLES = True if os.environ.get("BUILD_EXAMPLES", "true") == "true" else False
if BUILD_EXAMPLES:
    extensions.extend(["sphinx_gallery.gen_gallery"])

print(f"{extensions=}")
