#
# Makefile for I-D update presentations
#
THEME=Nord
SHELL=/bin/bash -O globstar

SRC:=$(wildcard *.md)

.PHONY: all
all: pdf

.PHONY: present
present:
	@echo "*** Starting Presentation ***"
	patat $(SRC)

.PHONY: present-float
present-float:
	@echo "*** Starting Presentation ***"
	alacritty --class patat_xfloating \
	          -o window.dimesions.columns=400 \
	          -o window.dimesions.lines=120 \
	          -o font.size=14.0 \
			  -o background_opacity=1 \
	          -e bash -ic 'patat -w $(SRC)'

.PHONY: pdf
PDF:=$(patsubst %.md,%.pdf,$(SRC))
pdf: $(PDF)

%.pdf: %.md
	@echo "*** Generating PDF Slide Deck $* ***"
	pandoc --to "beamer" \
	       --pdf-engine xelatex \
	       --output "$@" \
	       --variable "theme:$(THEME)" \
	       --incremental \
	       "$^"

.PHONY: clean
clean:
	@echo "*** Cleaning up ***"
	rm -rf $(PDF)
