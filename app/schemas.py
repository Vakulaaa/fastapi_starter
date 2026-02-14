from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)
    is_done: bool | None = None


class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    is_done: bool

    model_config = {"from_attributes": True}
