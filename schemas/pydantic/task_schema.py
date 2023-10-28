from typing import List

from pydantic import BaseModel


class TaskSchema(BaseModel):
    name: str
    dependencies: List[str]


class SearchTasksSchema(BaseModel):
    build: str
