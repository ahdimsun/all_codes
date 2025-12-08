from fastapi import FastAPI
from core.api_route.prayer_time_route import router as prayer_router

app = FastAPI()

app.include_router(prayer_router)