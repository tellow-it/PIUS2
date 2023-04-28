from webapps.customers import route_customers
from fastapi import APIRouter

web_router = APIRouter()
web_router.include_router(route_customers.router, prefix="", tags=["customers-webapp"])
