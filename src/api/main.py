from fastapi import FastAPI

from src.api.routes import router

app = FastAPI(
    title="AppX AI Assistant",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message":
        "AppX AI Assistant API Running"
    }