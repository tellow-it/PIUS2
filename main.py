from fastapi import FastAPI
from apis.base import api_router
from core.config import settings
from db.base import Base
from db.session import engine


def include_routers(application: FastAPI):
    application.include_router(api_router)


def create_tables():
    print('Creating tables...')
    Base.metadata.create_all(bind=engine)
    print('Success create tables!')


def start_application():
    application = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_routers(application)
    return application


app = start_application()
