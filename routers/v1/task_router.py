from typing import List, Optional

from fastapi import APIRouter, Depends, status, Request

from schemas.pydantic.task_schema import SearchTasksSchema
from services.task_service import TaskService

task_router = APIRouter(
    prefix="/v1/tasks", tags=["task"]
)


@task_router.post(
    "/",
    response_model=List[str],
    status_code=status.HTTP_200_OK,
)
async def tasks(
        request: Request,
        build: SearchTasksSchema,
        task_service: TaskService = Depends(),
):
    return task_service.tasks(request.state.builds_data, build)
