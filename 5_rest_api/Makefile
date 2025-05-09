up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

build:
	docker-compose build

run-backend:
	docker-compose exec django sh -c "pip install -r requirements.txt && python manage.py migrate && uvicorn --host 0.0.0.0 --reload exam_app.asgi:application"

migrations:
	docker-compose up -d django
	docker-compose exec django python manage.py makemigrations $(filter-out $@,$(MAKECMDGOALS))
	
.migrations:
	docker-compose exec django python manage.py makemigrations 

migrate:
	docker-compose exec django python manage.py migrate $(filter-out $@,$(MAKECMDGOALS))

.migrate:
	docker-compose up -d django
	docker-compose exec django python manage.py migrate

.migrate-migrations: .migrations .migrate

delete-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete

.reset-db:
	docker-compose up -d django
	docker-compose up -d postgres
	docker-compose exec postgres dropdb -U postgres --if-exists db_school
	docker-compose exec postgres createdb -U postgres db_school

reset-db: .reset-db .migrate-migrations

init_data:
	docker-compose run --rm django python manage.py init_data

gen-swagger-json:
	docker-compose exec django python manage.py generate_swagger --format json --output api-docs.json

collectstatic:
	docker-compose exec django python manage.py collectstatic