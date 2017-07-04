# app/Makefile
#
# :copyright: (c) 2017 Derek M. Frank
# :license: MPL-2.0
SHELL := /usr/bin/env zsh
PROJECT := roshi
TEST_PROJECT := tests

VENVDIR := venv
# We could already have venv activated, so check first.
ifeq ($(findstring $(VENVDIR)/bin:, $(PATH)), $(VENVDIR)/bin:)
	VENV :=
else
	VENV := . $(VENVDIR)/bin/activate;
endif

PY := $(VENV) python3
PIP := $(PY) -m pip
#PYI := ipython3
PYI := $(PY) -m bpython
LINTER := $(PY) -m pylint
TESTER := $(PY) -m pytest
CHECKER := $(PY) -m mypy

.PHONY: all
all: install

$(VENVDIR)/bin/activate:
	$(PY) -m venv $(VENVDIR)
	@ touch $(VENVDIR)/bin/activate

requirements.txt: $(VENVDIR)/bin/activate
	$(PIP) install -Ur requirements.txt
	@ touch requirements.txt

.PHONY: install
install: requirements.txt

.PHONY: run
run: install
	$(PY) entry.py
	# $(PY) manage.py runserver -h 0.0.0.0 -d -r

.PHONY: py
py: install
	$(PYI)  # $(PY) manage.py shell

.PHONY: sh
sh: install
	$(SHELL)

.PHONY: check-all
check-all: lint check test

.PHONY: lint
lint: install
	@ $(LINTER) *.py $(PROJECT) $(TEST_PROJECT)

.PHONY: check
check: install
	@ $(CHECKER) *.py
	@ $(CHECKER) -p $(PROJECT)
	@ $(CHECKER) -p $(TEST_PROJECT)

.PHONY: test tests
tests: test
test: install
	@ $(TESTER) $(TEST_PROJECT)

.PHONY: clean
clean: dist-clean
	@ find . -not \( -path "*/.git" -prune \) \
		\( -name '*.pyc' -or -name '*.pyo' -or -name '__pycache__' \) \
		-exec rm -rfv {} + \
			| wc -l | xargs echo 'Compiled Python files removed:'

.PHONY: dist-clean
dist-clean:
	@ rm -rfv *.egg-info \
		| wc -l | xargs echo 'Python distribution files removed:'
