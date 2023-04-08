# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = delta_docs_example
SOURCEDIR     = source
EXAMPLESDIR   = $(SOURCEDIR)/examples
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

examples:
	@echo "Building Python examples..."
	cp -r $(EXAMPLESDIR) $(BUILDDIR)
	jupytext $(BUILDDIR)/examples/*.md --to py
	rm -f $(BUILDDIR)/examples/*.md $(BUILDDIR)/examples/*.rst
	@echo "Done!"
