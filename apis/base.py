from fastapi import APIRouter
from apis.version1 import route_customers, route_addresses

api_router = APIRouter()

api_router.include_router(route_customers.router, prefix="/customers", tags=["customers"])
api_router.include_router(route_addresses.router, prefix="/addresses", tags=["addresses"])
