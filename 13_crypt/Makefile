include ../common.mk

ENCRYPT_FWD=${MIGRATIONS}/03_fwd_encrypt_passwords.sql
ENCRYPT_BWD=${MIGRATIONS}/03_bwd_encrypt_passwords.sql

## migrate_short: apply migrations from previous lessons
migrate_short:
	cp ${DB_BASE} ${DB_TEMP}
	${RUN_MIGRATE} --forward --db ${DB_TEMP} --limit 02

## migrate_all: apply migrations up to and including this lesson
migrate_all:
	cp ${DB_BASE} ${DB_TEMP}
	${RUN_MIGRATE} --forward --db ${DB_TEMP} --limit 03

## encrypt: create secret and migration to encrypt passwords
encrypt:
	make migrate_short
	DATA=${DB_TEMP} python generate_encryption.py \
	--secret secret.txt \
	--fwd 03_fwd_encrypt_passwords.sql \
	--bwd 03_bwd_encrypt_passwords.sql \
	--migrations ${MIGRATIONS} \
	--secret-value 102938474

## simple: run simple server
simple:
	make migrate_short
	${RUN_TEMP} server_simple.py run

## secure: run secure server
secure:
	make migrate_all
	SECRET=$$(cat secret.txt) DATA=temp.db flask --app server_secure.py run
