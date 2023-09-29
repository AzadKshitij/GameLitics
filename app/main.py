from fastapi import FastAPI
import logging
from starlette.middleware.cors import CORSMiddleware
from app.core.config import config
from app.api.api import api_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(" Creating GameLitics app instance ")

app = FastAPI(
    title=config.get("PROJECT_NAME"),
)
app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in config.get("BACKEND_CORS_ORIGINS")],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

app.include_router(api_router) # , prefix=settings.API_V1_STR)

@app.get("/")
def root():
    logger.info("Hello World")
    return {"message": "Hello World"}