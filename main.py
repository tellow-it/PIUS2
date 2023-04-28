from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from apis.base import api_router
from webapps.base import web_router

from core.config import settings
from db.base import Base
from db.session import engine


def include_routers(application: FastAPI):
    application.include_router(api_router)
    application.include_router(web_router)


def configure_static(application):
    application.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
    print('Creating tables...')
    Base.metadata.create_all(bind=engine)
    print('Success create tables!')


def start_application():
    application = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    configure_static(application)
    include_routers(application)
    create_tables()
    return application


app = start_application()
