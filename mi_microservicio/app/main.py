from fastapi import FastAPI
from app.api.routes import router
from app.config import Config

app = FastAPI(title=Config.APP_NAME)
app.include_router(router)