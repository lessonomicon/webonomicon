include ../common.mk

PLAIN_FWD=${MIGRATIONS}/02_fwd_add_plaintext_passwords.sql

## generate: create passwords and add to database
generate:
	DATA=${DB_BASE} python generate_accounts.py --seed 42179843 --template add_plaintext_passwords.sql > ${PLAIN_FWD}

## migrate: apply migrations
migrate:
	cp ${DB_BASE} ${DB_TEMP}
	${RUN_MIGRATE} --forward --db ${DB_TEMP} --verbose --limit 02

## serve: run server
serve:
	make migrate
	${RUN_TEMP} server.py run
