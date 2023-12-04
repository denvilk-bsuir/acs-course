from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.api import app as app_v1

app = FastAPI()

origins = [
    # 'http://localhost:5173',
    # 'localhost:5173',
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.mount('/v1', app_v1)

@app.get('/ping')
async def ping():
    return {'message':'pong'}
