include ../common.mk

## serve: run server
serve:
	cp ${DB_BASE} ${DB_TEMP}
	${RUN_MIGRATE} --forward --db ${DB_TEMP} --limit 03
	TXLATE=site_translation.json SECRET=$$(cat secret.txt) DATA=temp.db flask --app server.py run

## test: run pytest on translation tests
test:
	python -m pytest test_translation.py

## lang_uc: run request_lang.py with lang=uc (uc=fictional lang, just display everything in UPPERCASE)
lang_uc:
	python request_lang.py --lang=uc
