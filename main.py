from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import engine
from app.database import models
from app.api import shortener, stat
from app.views import shortener_views, stat_views


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def configure():
    configure_db()
    configure_routing()


def configure_routing():
    app.include_router(shortener.router)
    app.include_router(stat.router)

    app.include_router(shortener_views.router)
    app.include_router(stat_views.router)


def configure_db():
    models.Base.metadata.create_all(bind=engine)


configure()
# if __name__ == "__main__":
#     uvicorn.run('main:app', host='0.0.0.0', port=8000)
