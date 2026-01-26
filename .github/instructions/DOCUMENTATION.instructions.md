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
│   ├── source/
│   │   ├── api/                    # Auto-generated API documentation
│   │   ├── examples/               # Sphinx-Gallery examples
│   │   ├── getting_started/        # Getting started guides
│   │   │   └── contribute/         # Contribution guidelines
│   │   ├── user_guide/             # Main user documentation
│   │   │   ├── tutorials/          # Tutorial sections
│   │   │   └── concepts/           # Conceptual explanations
│   │   ├── _static/                # Static assets (images, CSS)
│   │   ├── conf.py                 # Sphinx configuration
│   │   ├── index.rst               # Main documentation entry point
│   │   └── links_and_refs.rst      # Shared references and substitutions
│   ├── styles/                     # Documentation styling
│   └── make.bat                    # Windows build script
└── examples/                       # Source example Python files
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

### 1. Creating a New Tutorial Section

Use when adding a completely new category of tutorials.

**Location**: `doc/source/user_guide/tutorials/new_section_name/`

**Steps**:

1. **Create section directory**:
   ```
   doc/source/user_guide/tutorials/new_section_name/
   ```

2. **Create `index.rst`** using the template:
   ```rst
   .. _ref_tutorial_new_section_template:

   =============
   Section title
   =============

   These tutorials demonstrate how to ...

   .. grid:: 1 1 3 3
       :gutter: 2
       :padding: 2
       :margin: 2

       .. grid-item-card:: Tutorial title
          :link: ref_tutorial_name
          :link-type: ref
          :text-align: center

          This tutorial shows how to...

          +++
          :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA` :bdg-fluent:`FLUENT` :bdg-cfx:`CFX`

   .. toctree::
       :maxdepth: 2
       :hidden:

       tutorial_file.rst
   ```

3. **Add to main toctree** in `doc/source/user_guide/index.rst`:
   ```rst
   .. toctree::
       :maxdepth: 2
       :hidden:
       :caption: Tutorials

       tutorials/existing_section/index.rst
       tutorials/new_section_name/index.rst
   ```

### 2. Creating a New Tutorial

**Location**: `doc/source/user_guide/tutorials/section_name/tutorial_name.rst`

**Template Structure**:
```rst
.. _ref_tutorial_name:

==============
Tutorial Title
==============

.. |api_name| replace:: :class:`ansys.dpf.core.class_name`

Single sentence describing the tutorial goal (matches card description).

Introduction providing context and foundational information.

:jupyter-download-script:`Download tutorial as Python script<tutorial_name>`
:jupyter-download-notebook:`Download tutorial as Jupyter notebook<tutorial_name>`

First Step
----------

First, you import the required modules and set up initial data...

.. jupyter-execute::

    # Import required modules
    from ansys.dpf import core as dpf
    
    # Define the result file path
    result_file_path = '/path/to/result.rst'

Second Step
-----------

Then, you create the necessary DPF objects...

.. jupyter-execute::

    # Create a DataSources object
    ds = dpf.DataSources(result_path=result_file_path)
    
    # Create a Model
    my_model = dpf.Model(data_sources=ds)

Final Step
----------

Finally, you achieve the tutorial objective...

.. jupyter-execute::

    # Get the results
    stress_fc = my_model.results.stress.eval()
    
    # Display information
    print(stress_fc)
```

**Add tutorial card** to section `index.rst`:
```rst
.. grid-item-card:: Tutorial Title
   :link: ref_tutorial_name
   :link-type: ref
   :text-align: center

   Brief description of what the tutorial teaches.

   +++
   :bdg-mapdl:`MAPDL` :bdg-lsdyna:`LS-DYNA`
```

**Add to toctree** in section `index.rst`:
```rst
.. toctree::
    :maxdepth: 2
    :hidden:

    existing_tutorial.rst
    tutorial_name.rst
```

### Tutorial Writing Guidelines

#### Code Blocks
- **Use `jupyter-execute`** for executable code blocks:
  ```rst
  .. jupyter-execute::

      # Comment explaining the code
      from ansys.dpf import core as dpf
  ```

- **Add comments** to clarify each line:
  ```python
  # Define the DataSources object
  ds = dpf.DataSources(result_path=result_file_path)
  ```

- **Name arguments explicitly**:
  ```python
  # Correct
  stress_fc = model.results.stress(time_scoping=time_steps).eval()
  
  # Incorrect
  stress_fc = model.results.stress(time_steps).eval()
  ```

- **Use proper API naming** in comments:
  ```python
  # Define the DataSources object  # Correct
  # Define the data sources object  # Incorrect
  ```

- **Add blank lines** between logical code sections:
  ```python
  # Define the result file path
  result_file_path = '/tmp/file.rst'

  # Define the DataSources object
  ds = dpf.DataSources(result_path=result_file_path)

  # Create a Model
  model = dpf.Model(data_sources=ds)
  ```

#### Text Formatting
- **Use API references** with substitution text:
  ```rst
  Here we use the |MeshedRegion| object...
  ```

- **Use bullet lists** for enumerations:
  ```rst
  This operator accepts:
  
  - A Result
  - An Operator  
  - A FieldsContainer
  ```

- **Use numbered lists** for sequential steps:
  ```rst
  To extract the mesh:
  
  #. Get the result file
  #. Create a Model
  #. Get the MeshedRegion
  ```

#### Solver-Specific Content
Use tabs for solver-specific implementations:

```rst
.. tab-set::

    .. tab-item:: MAPDL

        For MAPDL results...

        .. jupyter-execute::

            # MAPDL-specific code

    .. tab-item:: LS-DYNA

        For LS-DYNA results...

        .. jupyter-execute::

            # LS-DYNA-specific code
```

#### Available Solver Badges
- `:bdg-mapdl:`MAPDL``
- `:bdg-lsdyna:`LS-DYNA``
- `:bdg-fluent:`FLUENT``
- `:bdg-cfx:`CFX``

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
- [ ] Toctrees include all new files
- [ ] Solver badges display correctly
- [ ] Download links work for tutorials

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