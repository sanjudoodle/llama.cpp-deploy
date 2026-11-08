import httpx
from fastapi import APIRouter, Request
from fastapi.routing import APIRoute

from llamacpp_deploy.routers import homepage

router = APIRouter(tags=["health"])
routers = [homepage.router]


@router.get("/health")
async def health(request: Request):
    results = {}
    async with httpx.AsyncClient(base_url=str(request.base_url), timeout=5.0) as client:
        for api_router in routers:
            for route in api_router.routes:
                if not isinstance(route, APIRoute) or "GET" not in route.methods:
                    continue

                try:
                    response = await client.get(route.path)
                    results[route.path] = response.status_code
                except httpx.RequestError:
                    results[route.path] = "UNREACHABLE"

    return results
