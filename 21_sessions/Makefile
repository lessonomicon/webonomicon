include ../common.mk

## migrate_sessions: apply migrations up to and including this lesson (including sessions table)
migrate_sessions:
	@if [ ! -f ${DB_TEMP} ]; then \
		cp ${DB_BASE} ${DB_TEMP}; \
		${RUN_MIGRATE} --forward --db ${DB_TEMP} --verbose --limit 04; \
	fi

## sessions: run secure server with persistent sessions
sessions:
	make migrate_sessions
	SECRET=$$(cat secret.txt) DATA=temp.db flask --app server_sessions.py run

## jwt: run secure server with JWT authentication
jwt:
	make migrate_sessions
	SECRET=$$(cat secret.txt) JWT_SECRET=$$(openssl rand -hex 32) DATA=temp.db flask --app server_secure_jwt.py run
