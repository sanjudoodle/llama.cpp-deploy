from fastapi import FastAPI

from llamacpp_deploy.routers import homepage, health

app = FastAPI()

routers = [homepage.router, health.router]

for api_router in routers:
    app.include_router(api_router)