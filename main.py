from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from database.database import engine
from database import models
from api import shortener, stat
from views import shortener_views, stat_views

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


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


if __name__ == "__main__":
    configure()
    uvicorn.run(app, host='localhost', port=8000)
else:
    configure()

