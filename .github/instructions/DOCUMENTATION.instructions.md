---
applyTo: "doc/source/**/*.rst, examples/**/*"
name: "PyDPF-Core Documentation Contribution Guide"
about: "Guidelines for contributing to PyDPF-Core documentation, including tutorials and examples."
---

# IMPORTANT: Code Authenticity Requirement

**All code examples, snippets, and API usage in this documentation must be strictly based on the actual PyDPF-Core API reference documentation or the code source base.**

- AI agents and human contributors must never invent, suggest, or use code that does not exist in the official API reference or codebase.
- Before including any code, always verify its existence and correctness in the API reference or source code.
- If a feature or method is not present in the API or codebase, do not document or reference it.

# PyDPF-Core Documentation Contribution Guide

This guide provides comprehensive instructions for contributing to the PyDPF-Core documentation, including how to add tutorials, examples, and other content.

## Overview

PyDPF-Core uses **Sphinx** with **reStructuredText (reST)** for documentation generation. The documentation follows a structured approach with four main functions:

- **Tutorials**: Learning-oriented, step-by-step guides for beginners
- **Examples**: Use-case oriented solutions to specific problems
- **Concepts**: Understanding-oriented theoretical explanations
- **API Reference**: Informing-oriented technical reference (auto-generated)

## Project Structure

```
pydpf-core/
├── doc/
│   ├── sphinx_gallery_tutorials/   # Source tutorial Python scripts
│   │   ├── index.rst               # Tutorials landing page
│   │   └── section_name/           # Tutorial section folder
│   │       ├── GALLERY_HEADER.rst  # Section landing page
│   │       └── tutorial_name.py    # Tutorial script
│   ├── source/
│   │   ├── api/                    # Auto-generated API documentation
│   │   ├── tutorials/              # Auto-generated tutorial pages (sphinx-gallery output)
│   │   ├── examples/               # Auto-generated example pages (sphinx-gallery output)
│   │   ├── getting_started/        # Getting started guides
│   │   │   └── contribute/         # Contribution guidelines
│   │   ├── user_guide/             # Main user documentation
│   │   │   └── concepts/           # Conceptual explanations
│   │   ├── _static/                # Static assets (images, CSS)
│   │   ├── conf.py                 # Sphinx configuration
│   │   ├── index.rst               # Main documentation entry point
│   │   └── links_and_refs.rst      # Shared references and substitutions
│   ├── styles/                     # Documentation styling
│   └── make.bat                    # Windows build script
```

## Prerequisites

1. **Setup Development Environment**: Follow the developer setup instructions in `doc/source/getting_started/contribute/developer.rst`
2. **Install Dependencies**: 
   ```bash
   python -m pip install tox tox-uv
   ```

## Building Documentation

### Using Tox (Recommended)

PyDPF-Core uses Tox for documentation building. Available environments:

- `doc-html`: Build HTML documentation
- `doc-clean`: Clean previous builds
- `doc-linkcheck`: Check external links

**Basic build:**
```bash
python -m tox -e doc-html
```

**Fast build (skip examples and API):**
```bash
python -m tox -e doc-html -x testenv:doc-html.setenv+="BUILD_API=false" -x testenv:doc-html.setenv+="BUILD_EXAMPLES=false"
```

### Using Make (Windows)

```bash
cd doc
make.bat html
make.bat clean  # Clean previous builds
```

## Adding Tutorials

Tutorials are Python scripts processed by [Sphinx-Gallery](https://sphinx-gallery.github.io/).
They live in `doc/sphinx_gallery_tutorials/` and are auto-converted to HTML pages, Jupyter notebooks,
and downloadable Python scripts during the build. **No manual toctree entries are ever needed** —
sphinx-gallery manages the navigation automatically.

### 1. Creating a new tutorial section

A tutorial **section** is a sub-folder of `doc/sphinx_gallery_tutorials/` that groups related tutorials.
Each section must contain a `GALLERY_HEADER.rst` file.

**Location**: `doc/sphinx_gallery_tutorials/new_section_name/`

**Steps**:

1. **Create the section directory**:
   ```
   doc/sphinx_gallery_tutorials/new_section_name/
   ```

2. **Create `GALLERY_HEADER.rst`**:

   ```rst
   .. _ref_tutorials_new_section_name:

   =================
   New section title
   =================

   Description of what the tutorials in this section cover.

   .. grid:: 1 1 3 3
       :gutter: 2
       :padding: 2
       :margin: 2

       .. grid-item-card:: Tutorial title
          :link: ref_tutorial_name
          :link-type: ref
          :text-align: center

          Brief description of the tutorial.

   .. raw:: html

      <style>.sphx-glr-thumbnails { display: none; }</style>
   ```

   The `<style>` block hides the auto-generated thumbnail row that sphinx-gallery adds;
   the grid cards above already serve as the section landing page navigation.

3. **Add a card** to `doc/sphinx_gallery_tutorials/index.rst` linking to the new section
   using the same `.. grid-item-card::` format as the existing sections and you
   must also add a toctree entry for the new section to the same file
   following the same ``tutorials/<section-name>/index`` pattern as the existing
   toctree entries.

### 2. Creating a new tutorial

Tutorials are Python scripts named `tutorial_name.py` in the corresponding section folder.

**Location**: `doc/sphinx_gallery_tutorials/section_name/tutorial_name.py`

**File structure** (in order):

1. **MIT license header** (21 lines — copy verbatim from any existing tutorial, updating the year range if needed).

2. **Ordering comment** (immediately after the blank line following the license):
   ```python
   # _order: 1
   ```
   Sets the position of this tutorial within its section (must be unique within the section).

3. **Module docstring** — the tutorial header:
   ```python
   """
   .. _ref_tutorial_name:

   Tutorial Title
   ==============

   Single sentence describing the tutorial goal (same as the card description).

   Longer introduction providing context and what the reader will learn.
   """
   ```

4. **Content cells** — separated by a line of exactly 79 `#` characters:
   ```python
   ###############################################################################
   # First Step
   # ----------
   #
   # First, you import the required modules and set up initial data.

   # Import required modules
   from ansys.dpf import core as dpf

   # Define the result file path
   result_url = dpf.core.examples.find_simple_bar()

   # Create a DataSources object
   ds = dpf.DataSources(result_path=result_url)

   # Create a Model
   my_model = dpf.Model(data_sources=ds)

   ###############################################################################
   # Second Step
   # -----------
   #
   # Then, you extract what you need from the model.

   # Get displacement results
   displacement_fc = my_model.results.displacement.eval()
   print(displacement_fc)

   ###############################################################################
   # Final Step
   # ----------
   #
   # Finally, you achieve the tutorial objective.

   # Plot the first displacement field
   displacement_fc[0].plot()
   ```

   In sphinx-gallery:
   - A cell separator (`###...`) followed by `# Title` / `# -----` lines becomes an RST section heading.
   - Consecutive `# `-prefixed lines in a cell (with no executable code between them) become RST prose.
   - Lines **without** a leading `#` are executed as Python code.

5. **Add a card** to the section's `GALLERY_HEADER.rst`:
   ```rst
   .. grid-item-card:: Tutorial Title
      :link: ref_tutorial_name
      :link-type: ref
      :text-align: center

      Brief description of what this tutorial teaches.
   ```

### Tutorial Writing Guidelines

#### Code style
- **Comment each logical block** with a `#` line above it:
  ```python
  # Define the DataSources object
  ds = dpf.DataSources(result_path=result_url)
  ```

- **Name arguments explicitly** when calling PyDPF-Core APIs:
  ```python
  # Correct
  stress_fc = my_model.results.stress(time_scoping=time_steps).eval()

  # Incorrect
  stress_fc = my_model.results.stress(time_steps).eval()
  ```

- **Use proper API names** in comments (capital letters for DPF class names):
  ```python
  # Define the DataSources object   ← correct
  # Define the data sources object  ← incorrect
  ```

- **Add blank lines** between logical groups of code lines.

- **Avoid naming variables** the same as a DPF class or argument name:
  ```python
  # Correct
  my_model = dpf.Model(data_sources=ds)

  # Incorrect
  model = dpf.Model(data_sources=model)
  ```

#### Text prose (RST comment blocks)
Prose before a code block is written as `# `-prefixed lines after the cell separator.
Full reStructuredText syntax is supported:

- **API cross-references** — use `|SubstitutionText|` from `doc/source/links_and_refs.rst`:
  ```python
  # Work with the |MeshedRegion| to extract nodal coordinates.
  ```

- **Bullet lists**:
  ```python
  # The operator accepts:
  #
  # - A Result
  # - An Operator
  # - A FieldsContainer
  ```

- **Numbered lists** for sequential steps:
  ```python
  # To extract the mesh:
  #
  # #. Get the result file
  # #. Create a Model
  # #. Get the MeshedRegion
  ```

## Adding Examples

Examples are standalone Python scripts in the `examples/` directory that use Sphinx-Gallery.

### Structure
- **Location**: `examples/XX-category/script_name.py`
- **Format**: Python scripts with reST docstrings
- **Auto-generated**: Jupyter notebooks and documentation pages

### Example Template
```python
"""
Example Title
=============

Explanation of the main topic with relevant keywords for SEO.

This example demonstrates how to...
"""

# sphinx_gallery_thumbnail_number = 2

###############################################################################
# Import required modules
# -----------------------
# First, import the necessary modules.

from ansys.dpf import core as dpf

###############################################################################
# Load the result file
# --------------------
# Load the result file and create a model.

# Define file path
result_file = dpf.download_file("file.rst", "downloads")

# Create model
model = dpf.Model(result_file)

###############################################################################
# Extract results
# ---------------
# Extract the desired results from the model.

# Get displacement results
displacement = model.results.displacement.eval()

# Display information
print(displacement)

###############################################################################
# Plotting
# --------
# Create plots to visualize the results.

displacement.plot()
```

### Adding Example Sections
When creating a new example category:

1. **Create directory**: `examples/XX-new-category/`
2. **Add README.txt**:
   ```
   Category Title
   ==============
   
   Description of the examples in this category.
   ```

## Content Guidelines

### Documentation Style
- Follow the [PyAnsys Documentation Style Guide](https://dev.docs.pyansys.com/guidelines/documentation.html)
- Use clear, concise language
- Maintain consistent terminology
- Include necessary context without overwhelming detail

### Technical Guidelines
- All code must be executable
- Use absolute file paths in examples
- Include error handling where appropriate
- Test all code examples before submission
- Follow PyDPF-Core coding standards

### File Organization
- Use lowercase names for files and directories
- Use descriptive, short names
- Maintain logical hierarchy
- All files must be included in toctrees (no dangling files)

## Available References

Common PyDPF-Core references are available in `doc/source/links_and_refs.rst`:

- `|MeshedRegion|` → Links to MeshedRegion API
- `|Field|` → Links to Field API
- `|FieldsContainer|` → Links to FieldsContainer API
- `|Model|` → Links to Model API
- And many more...

## Testing Documentation

### Local Testing
1. **Build documentation**:
   ```bash
   python -m tox -e doc-html
   ```

2. **Check output**: `doc/build/html/index.html`

3. **Verify links**:
   ```bash
   python -m tox -e doc-linkcheck
   ```

### Validation Checklist
- [ ] All code blocks execute without errors
- [ ] All internal links work correctly
- [ ] Images display properly
- [ ] Tutorial cards render correctly
- [ ] Solver badges display correctly (if used)
- [ ] Downloads (`.py` and `.ipynb`) work for tutorials

## Submission Process

1. **Create branch**: `git checkout -b feature/doc-contribution`
2. **Make changes**: Add tutorials/examples following guidelines
3. **Test locally**: Build docs and verify functionality
4. **Commit changes**: Use descriptive commit messages
5. **Create PR**: Include description of changes and testing performed

## Common Issues and Solutions

### Build Errors
- **Missing toctree entries**: Ensure all `.rst` files are included in toctrees
- **Invalid references**: Check reference tags match file structure
- **Code execution failures**: Verify all code blocks are executable

### Formatting Issues
- **Inconsistent indentation**: Use spaces, maintain consistent indentation
- **Missing blank lines**: Add blank lines between sections and code blocks
- **Invalid reST syntax**: Check directive formatting and closing tags

## Additional Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Sphinx-Gallery Documentation](https://sphinx-gallery.github.io/)
- [PyAnsys Developer's Guide](https://dev.docs.pyansys.com/)
- [PyDPF-Core Documentation](https://dpf.docs.pyansys.com/)

## Contact

For questions about documentation contributions:
- **Email**: [pyansys.core@ansys.com](mailto:pyansys.core@ansys.com)
- **Issues**: [PyDPF-Core Issues](https://github.com/ansys/pydpf-core/issues)
- **Discussions**: [PyDPF-Core Discussions](https://github.com/ansys/pydpf-core/discussions)