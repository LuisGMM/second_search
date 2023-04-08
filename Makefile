# The following Makefile holds different useful rules for automating several
# tasks such us checking code quality, testing and code coverage

# Make sure a rule is executed even if no file changes are detected
.PHONY: docs

# The general and default rule for running all available ones.
all: docs

docs:
	$(MAKE) -C docs/ html
