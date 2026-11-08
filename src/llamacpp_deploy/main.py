from fastapi import FastAPI

from llamacpp_deploy.routers import chat, health, homepage

app = FastAPI()

routers = [homepage.router, health.router, chat.router]

for api_router in routers:
    app.include_router(api_router)
