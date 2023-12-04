from fastapi import FastAPI
from .stats import router

app = FastAPI(
    title="Prodigy VPN stats API v1",
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
)

app.include_router(router)
