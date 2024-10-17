include ../common.mk

## split: explore data insertion with split operations
split:
	cp ${DB_BASE} ${DB_TEMP}
	DATA=${DB_TEMP} python explore_insert.py something random split

## combined: explore data insertion with combined operations
combined:
	cp ${DB_BASE} ${DB_TEMP}
	DATA=${DB_TEMP} python explore_insert.py something random combined

## serve: make fresh database and run server
serve:
	cp ${DB_BASE} ${DB_TEMP}
	${RUN_TEMP} server.py run
