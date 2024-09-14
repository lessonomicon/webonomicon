# Runnable tasks.

include common.mk

all: commands

# CSS=-css chota.css
# CSS=-css neat.css
# CSS=-css picnic.css
# CSS=-css pico.css
# CSS=-css simple.css
# CSS=-css tacit.css
CSS=
HTML_IGNORES = 'Attribute "x-' 'Attribute "@click' 'Attribute "file"'

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

## render: convert to HTML
render:
	mccole render ${CSS}
	@touch docs/.nojekyll

## refresh: convert to HTML, refreshing code samples
refresh:
	mccole render --refresh ${CSS}
	@touch docs/.nojekyll

## serve: serve generated HTML
serve:
	@python -m http.server -d docs $(PORT)

## stats: basic site statistics
stats:
	@mccole stats
