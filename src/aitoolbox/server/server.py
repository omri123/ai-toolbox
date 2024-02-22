import uvicorn
from fastapi import FastAPI


def main():
    app = FastAPI()

    @app.get("/msg/")
    async def msg():
        return {"message": "Hello World"}

    uvicorn.run(app)


if __name__ == '__main__':
    main()
