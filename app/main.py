from fastapi import FastAPI

from .database import Base, engine
from .routers.tasks import router as tasks_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI + SQLite Tutorial")


@app.get("/")
def healthcheck():
    return {"status": "ok"}


app.include_router(tasks_router)
