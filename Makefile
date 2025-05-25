.PHONY: install
install:
	poetry install


.PHONY: migrate
migrate:
	poetry run python3 manage.py migrate


.PHONY: migrations
migrations:
	poetry run python3 manage.py makemigrations

.PHONY: run-server
run-server:
	poetry run python3 manage.py runserver 8001

.PHONY: createsuperuser
superuser:
	poetry run python3 manage.py createsuperuser

.PHONY: update
update: install	migrations	migrate run-server static

.PHONY: backup-db
load-db-backup:
	poetry run python3 manage.py loaddata dump.json	

.PHONY: create-dump-db	
create-dump-db:
	poetry run python3 manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > dump.json

.PHONY: static
static:
	python3 manage.py collectstatic

