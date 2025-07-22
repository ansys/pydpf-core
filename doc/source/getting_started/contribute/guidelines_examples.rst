.. _ref_guidelines_examples:

=================
Writing examples
=================

The documentation generator used in PyDPF-Core is `Sphinx`_. Most of the documents
are written in `reStructuredText`_. Some parts of the documentation, like the
:ref:`examples <Examples>`, use a mix of `reStructuredText`_ and Python, thanks to `Sphinx-Gallery`_.

The :ref:`examples <Examples>` section of the documentation showcases different
capabilities of PyDPF-Core. Each example (grouped into folders of related examples)
is a standalone Python script. Despite being ``*.py`` files, they are written in a mix
of `reStructuredText`_ and Python. This is possible thanks to the `Sphinx-Gallery`_
Sphinx extension.

Documentarians writing new examples are encouraged to familiarize themselves with
`structuring Python scripts for Sphinx-Gallery <https://sphinx-gallery.github.io/stable/syntax.html>`_.
Once the ``.py`` file for a new example is properly set up, Sphinx-Gallery automatically
generates `Sphinx`_ `reStructuredText`_ files from it. The rendering of the resulting reST will provide
users with ``.ipynb`` (Jupyter notebook) and ``.py`` files of each example, which users can download.

Finally, here are some tips for writing examples:

- Start the example with an explanation of the main topic. Try to use as many relevant
  keywords as possible in this section to optimize for Search Engine Optimization.

- Include an explanation with each code cell. The explanations should
  be included before, not after, the corresponding code.

- The examples are built with the documentation. As part of the build process,
  screenshots of rendered graphics are inserted in the document. You do not need
  to include the screenshots yourself.

- When creating a new folder where more than one related example will be included, ensure
  a ``README.txt`` file is also included. This file should contain reST to be used as the header
  for the index page corresponding to the subsection for these examples in the generated documentation.