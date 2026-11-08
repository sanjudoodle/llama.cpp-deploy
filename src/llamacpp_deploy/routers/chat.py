from fastapi import APIRouter, HTTPException
from openai import OpenAI, OpenAIError
from pydantic import BaseModel, Field

from llamacpp_deploy.config import LLAMACPP_URL

router = APIRouter(tags=["chat"])


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=500)


class ChatResponse(BaseModel):
    reply: str


llama_url = LLAMACPP_URL.rstrip("/")
llama_url = llama_url if llama_url.endswith("/v1") else f"{llama_url}/v1"

model = OpenAI(base_url=llama_url, api_key="no-key", timeout=30, max_retries=0)


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        response = model.chat.completions.create(
            model="local",
            messages=[{"role": "user", "content": request.message}],
            max_tokens=128,
        )
    except OpenAIError:
        raise HTTPException(status_code=502, detail="LLM unreachable")

    return {"reply": response.choices[0].message.content or "Unable to generate text"}
