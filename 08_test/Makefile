include ../common.mk

## test: run all tests
test:
	pytest .

## test_heartbeat: basic test of heartbeat from server
test_heartbeat:
	pytest test_heartbeat.py

## test_fixtures: rewrite heartbeat test with fixtures
test_fixtures:
	pytest test_fixtures.py

## test_db: use function patching
test_db:
	pytest test_db.py

## test_combined: combine the two approaches
test_combined:
	pytest test_combined.py
