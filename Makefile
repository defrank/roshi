# Inspired by: http://www.lackof.org/taggart/hacking/make-example/
SHELL := /usr/bin/env zsh

DIRS := $(foreach p,$(wildcard */Makefile),$(shell dirname $(p)))
BUILDDIRS := $(DIRS:%=build-%)
INSTALLDIRS := $(DIRS:%=install-%)
RUNDIRS := $(DIRS:%=run-%)
LINTDIRS := $(DIRS:%=lint-%)
CLEANDIRS := $(DIRS:%=clean-%)
TESTDIRS := $(DIRS:%=test-%)

.PHONY: all $(DIRS) $(BUILDDIRS)
all: install $(BUILDDIRS)
$(DIRS): $(BUILDDIRS)
$(BUILDDIRS):
	@ $(MAKE) -C $(@:build-%=%)
	docker-compose build

.PHONY: install $(INSTALLDIRS)
install: $(INSTALLDIRS)
$(INSTALLDIRS):
	@ $(MAKE) -C $(@:install-%=%) install

.PHONY: up run
up: run
run: all
	docker-compose up

.PHONY: upd rund
upd: rund
rund: all
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: py
py: rund
	docker-compose exec app python3

.PHONY: sh
sh: rund
	docker-compose exec app /bin/sh

.PHONY: lint $(LINTDIRS)
lint: install $(LINTDIRS)
$(LINTDIRS):
	@ $(MAKE) -C $(@:lint-%=%) lint

.PHONY: test $(TESTDIRS)
test: all $(TESTDIRS)
$(TESTDIRS):
	@ $(MAKE) -C $(@:test-%=%) test

.PHONY: clean-all
clean-all: down clean

.PHONY: clean $(CLEANDIRS)
clean: dist-clean $(CLEANDIRS)
$(CLEANDIRS):
	@ $(MAKE) -C $(@:clean-%=%) clean

.PHONY: dist-clean
dist-clean:
	@ find . -not \( -path "*/.git" -prune \) \
		-type d \( -name "build" -or -name "dist" \) \
		-exec rm -rfv {} + \
			| wc -l | xargs echo 'Distribution files removed:'

.PHONY: docs
docs:
	grip
