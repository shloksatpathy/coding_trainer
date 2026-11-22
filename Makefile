# Build system for Coding Trainer. Run `make` to list the targets.
# Never touches your own files: work/ (your solutions) and progress.json.

# CLI, web app and tests
PYTHON     ?= python3
# Desktop app: needs GTK 3 bindings (python3-gi, preinstalled on Ubuntu)
GUI_PYTHON ?= /usr/bin/python3
VERSION    := $(shell cat VERSION)
DIST       := build/coding-trainer-$(VERSION).tar.gz

.PHONY: help run web install uninstall test dist clean

help:
	@echo "make run        start the desktop app"
	@echo "make web        start the web app on http://localhost:8000"
	@echo "make install    add Coding Trainer to your app grid"
	@echo "make uninstall  remove it from your app grid"
	@echo "make test       check generators and all 84 reference solutions (in a temp copy)"
	@echo "make dist       package the committed project as $(DIST)"
	@echo "make clean      remove build/, cache/ and __pycache__/"

run:
	$(GUI_PYTHON) gui.py

web:
	$(PYTHON) app.py

install:
	./install-desktop.sh

uninstall:
	rm -f $(HOME)/.local/share/applications/coding-trainer.desktop

test:
	$(PYTHON) selftest.py

dist: test
	mkdir -p build
	git archive --prefix=coding-trainer-$(VERSION)/ -o $(DIST) HEAD
	@echo "Built $(DIST) ($$(du -h $(DIST) | cut -f1))"

clean:
	rm -rf build cache __pycache__
