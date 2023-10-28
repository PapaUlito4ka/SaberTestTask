from collections import deque
from typing import List

from fastapi import HTTPException, status

from configs.builds_data import BuildsData
from schemas.pydantic.task_schema import SearchTasksSchema


class TaskService:

    def tasks(self, builds_data: BuildsData,  build_: SearchTasksSchema) -> List[str]:
        build_name = build_.build
        build = builds_data.builds.get(build_name)
        if build is None:
            raise HTTPException(
                detail=f"Build '{build_name}' does not exist.",
                status_code=status.HTTP_404_NOT_FOUND
            )

        tasks = deque(build.tasks)
        res_tasks: List[str] = []

        while len(tasks) > 0:
            task_name = tasks.popleft()
            task = builds_data.tasks.get(task_name)
            if task is None:
                raise HTTPException(
                    detail=f"Task '{task_name}' does not exist.",
                    status_code=status.HTTP_404_NOT_FOUND
                )

            task_dependencies = task.dependencies
            if len(task_dependencies) == 0:
                res_tasks.append(task_name)
                continue

            for i in range(len(task_dependencies) - 1, -1, -1):
                tasks.appendleft(task_dependencies[i])

        return res_tasks
