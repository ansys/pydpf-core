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
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


# customized clean
clean:
	rm -rf $(BUILDDIR)/*
	rm -rf source/examples/
	find . -type d -name "_autosummary" -exec rm -rf {} +

# customized to build the pdf rather than using latexpdf due to various issues
# with our docs like GIFs being written as PNG.
pdf:
	@$(SPHINXBUILD) -M latex "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	cd build/latex && latexmk -r latexmkrc -pdf *.tex -interaction=nonstopmode || true
	(test -f build/latex/*.pdf && echo pdf exists) || exit 1

# customized clean due to examples gallery
clean-except-examples:
	rm -rf $(BUILDDIR)/*
	rm -rf images/auto-generated
	find . -type d -name "_autosummary" -exec rm -rf {} +
