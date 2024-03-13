import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, PlainTextResponse
from openai import OpenAI
from aitoolbox.server.state import ConvesationState
from aitoolbox.server.llm import state2openai
from pydantic import BaseModel


class UserMsg(BaseModel):
    content: str
    forget: bool
    sysmsg1: str
    sysmsg2: str


client = OpenAI()
state = ConvesationState()


def get_app():
    app = FastAPI()

    @app.post("/msg/")
    async def msg(user_msg: UserMsg):
        async def response_generator():
            messages = state2openai(state, user_msg.sysmsg1, user_msg.sysmsg2)
            messages.append({"role": "user", "content": user_msg.content})
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                stream=True
            )
            response_content = []
            for chunk in stream:
                chunk_content = chunk.choices[0].delta.content
                if chunk_content is not None:
                    response_content.append(chunk_content)
                    yield chunk_content

            if not user_msg.forget:
                state.add_msg("user", user_msg.content)
                state.add_msg("assistant", "".join(response_content))

        return StreamingResponse(response_generator())

    @app.get("/history/")
    async def history():
        return PlainTextResponse(str(state))

    return app


def main():
    app = get_app()
    uvicorn.run(app)
