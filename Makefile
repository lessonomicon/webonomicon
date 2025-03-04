# Runnable tasks.

include common.mk

all: commands

HTML_IGNORES = 'Attribute "x-' 'Attribute "@click' 'Attribute "file"'

## build: build HTML
build:
	mccole build
	@touch docs/.nojekyll

## datasets: re-create snailz parameters and datasets
datasets:
	snailz params --outdir params
	snailz everything --paramsdir params --datadir data

## lint: check code and project
lint:
	@ruff check --exclude docs .
	@mccole lint
	@html5validator --root docs --blacklist templates --ignore ${HTML_IGNORES} \
	&& echo "HTML checks passed."

## profile: render with profiling
profile:
	mccole profile
	@touch docs/.nojekyll

## refresh: refresh all file inclusions
refresh:
	mccole refresh --files *_*/index.md

## serve: serve generated HTML
serve:
	@python -m http.server -d docs $(PORT)

## stats: basic site statistics
stats:
	@mccole stats
