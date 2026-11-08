from fastapi import APIRouter
from openai import OpenAI

from llamacpp_deploy.config import LLAMACPP_URL

router = APIRouter(tags=["chat"])

model = OpenAI(base_url=LLAMACPP_URL, api_key="no-key")


@router.post("/chat")
def chat():
    return "chat"
