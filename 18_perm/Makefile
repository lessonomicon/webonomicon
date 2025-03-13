include ../common.mk

## json: test JSON
json:
	cp ${DB_BASE} ${DB_TEMP}
	${RUN_MIGRATE} --forward --limit 02 --db ${DB_TEMP}
	DB=${DB_TEMP} pytest test_json.py

## perm: test permissions
perm:
	cp ${DB_BASE} ${DB_TEMP}
	${RUN_MIGRATE} --forward --limit 02 --db ${DB_TEMP}
	DB=${DB_TEMP} pytest test_permissions.py
