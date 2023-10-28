from typing import List

from pydantic import BaseModel


class BuildSchema(BaseModel):
    name: str
    tasks: List[str]

