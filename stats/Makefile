run:
	uvicorn main:app --reload --port 8000

makemigrations:
# @echo $(msg)
	alembic revision --autogenerate -m "$(msg)"

migrate:
	alembic upgrade head