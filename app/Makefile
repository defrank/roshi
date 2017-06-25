SHELL := /usr/bin/env zsh
PROJECT := roshi

PY := python3
PIP := $(PY) -m pip
#PYI := ipython3
PYI := $(PY) -m bpython

VENVDIR := venv
# We could already have venv activated, so check first.
ifeq ($(findstring $(VENVDIR)/bin:, $(PATH)), $(VENVDIR)/bin:)
	VENV :=
else
	VENV := . $(VENVDIR)/bin/activate;
endif

LINTERS := flake8 pylint
TESTERS := pytest
CHECKERS := mypy

.PHONY: all
all: install

$(VENVDIR)/bin/activate:
	$(PY) -m venv $(VENVDIR)
	@ touch $(VENVDIR)/bin/activate

requirements.txt: $(VENVDIR)/bin/activate
	$(VENV) $(PIP) install -Ur requirements.txt
	@ touch requirements.txt

.PHONY: install
install: requirements.txt

.PHONY: run
run: install
	$(VENV) # $(PY) manage.py runserver -h 0.0.0.0 -d -r

.PHONY: py
py: install
	$(VENV) $(PYI)  # $(PY) manage.py shell

.PHONY: sh
sh: install
	$(VENV) $(SHELL)

.PHONY: check-all
check-all: lint check test

.PHONY: lint
lint: install
	@ $(VENV) set -e; for linter in $(LINTERS); do \
		print $$linter >&2; \
		$(PY) -m $$linter *.py $(PROJECT); \
	done

.PHONY: check
check: install
	@ $(VENV) set -e; for checker in $(CHECKERS); do \
		print $$checker >&2; \
		$(PY) -m $$checker *.py $(PROJECT); \
	done

.PHONY: test tests
tests: test
test: install
	@ $(VENV) set -e; for tester in $(TESTERS); do \
		print $$tester >&2; \
		$(PY) -m $$tester tests; \
	done

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
