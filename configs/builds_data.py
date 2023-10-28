from contextlib import asynccontextmanager
from typing import List, Dict

from pydantic import BaseModel

from schemas.pydantic.build_schema import BuildSchema
from schemas.pydantic.task_schema import TaskSchema
from services.builds_data_service import BuildsDataService


class BuildsData(BaseModel):
    builds: Dict[str, BuildSchema]
    tasks: Dict[str, TaskSchema]


def get_builds_data():
    return BuildsData(
        builds=BuildsDataService.get_builds(),
        tasks=BuildsDataService.get_tasks()
    )


@asynccontextmanager
async def lifespan(app):
    yield {
        'builds_data': get_builds_data()
    }
