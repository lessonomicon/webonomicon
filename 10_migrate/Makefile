include ../common.mk

## forward: migrate database forward
forward:
	cp ${DB_BASE} ${DB_TEMP}
	${RUN_MIGRATE} --forward --db ${DB_TEMP} --verbose --limit 01

## backward: revert database
backward:
	${RUN_MIGRATE} --backward --db ${DB_TEMP} --verbose --limit 01
