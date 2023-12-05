#!/bin/bash
cd /app/
alembic upgrade head

cd /app
uvicorn main:app --host 0.0.0.0 --port 8000
exec "$@"