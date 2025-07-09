# Simple makefile to simplify repetitive build env management tasks under posix

CODESPELL_DIRS ?= ./
CODESPELL_SKIP ?= "*.pyc,*.txt,*.gif,*.png,*.jpg,*.js,*.html,*.doctree,*.ttf,*.woff,*.woff2,*.eot,*.mp4,*.inv,*.pickle,*.ipynb,flycheck*,./.git/*,./.hypothesis/*,*.yml,./doc/build/*,./doc/images/*,./dist/*,*~,.hypothesis*,./doc/source/examples/*,*cover,*.dat,*.mac,\#*,build,./ansys/dpf/core/raw_operators.py,./run_client.bat,./docker/v211"
CODESPELL_IGNORE ?= "ignore_words.txt"

all: doctest

doctest: codespell

codespell:
	@echo "Running codespell"
	@codespell $(CODESPELL_DIRS) -S $(CODESPELL_SKIP) -I $(CODESPELL_IGNORE)

flake8:
	@echo "Running flake8"
	@flake8 .

pydocstyle:
	@echo "Running pydocstyle"
	@pydocstyle ansys.dpf.core

doctest-modules:
	@echo "Running module doctesting"
	pytest -v --doctest-modules ansys.dpf.core

coverage:
	@echo "Running coverage"
	@pytest -v --cov ansys.dpf.core

coverage-xml:
	@echo "Reporting XML coverage"
	@pytest -v --cov ansys.dpf.core --cov-report xml

coverage-html:
	@echo "Reporting HTML coverage"
	@pytest -v --cov ansys.dpf.core --cov-report html
