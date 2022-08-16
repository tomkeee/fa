makemigrations:
	docker-compose exec backend bash -c "alembic revision --autogenerate"

migrate:
	docker-compose exec backend bash -c "alembic upgrade head"