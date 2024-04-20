from fastapi import FastAPI

from weather.router import router

app = FastAPI()

app.include_router(
    router=router, prefix="/weather", tags=["Weather"]
)


@app.get("/",)
def read_root() -> dict:
    return {"message": "Hello World"}
