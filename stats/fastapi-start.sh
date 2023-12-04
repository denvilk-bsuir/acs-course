python3 -m venv .venv
source .venv/bin/activate
pip install uvicorn fastapi sqlalchemy asyncpg 

mkdir api
mkdir core
mkdir models
mkdir services

touch core/__init__.py
touch api/__init__.py
touch models/__init__.py
touch services/__init__.py

touch req.txt
touch main.py
touch .dockerignore
touch Dockerfile
touch core/config.py
touch core/connections.py
touch core/exceptions.py
touch core/security.py
touch models/schemas.py
