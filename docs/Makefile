# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -j auto
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -v -v -v -P -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -v -v -v -P -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


# customized clean
clean:
	rm -rf $(BUILDDIR)
	rm -rf $(SOURCEDIR)/images/auto-generated
	cp -r -v $(SOURCEDIR)/examples/07-python-operators/plugins $(TEMP)
	rm -rf $(SOURCEDIR)/examples
	cp -r -v $(TEMP)/plugins $(SOURCEDIR)/examples/07-python-operators
	rm -rf $(TEMP)
