from typing import List, Dict

import yaml

from configs.logger import get_logger
from schemas.pydantic.build_schema import BuildSchema
from schemas.pydantic.task_schema import TaskSchema

logger = get_logger()


class BuildsDataService:

    @staticmethod
    def get_builds() -> Dict[str, BuildSchema]:
        try:
            with open('builds/builds.yaml', 'r') as file:
                raw_data = yaml.safe_load(file)
                raw_builds = raw_data["builds"]
                return {raw_build["name"]: BuildSchema(**raw_build) for raw_build in raw_builds}
        except Exception as e:
            logger.error("Error while parsing builds.yaml")
            raise

    @staticmethod
    def get_tasks() -> Dict[str, TaskSchema]:
        try:
            with open('builds/tasks.yaml', 'r') as file:
                raw_data = yaml.safe_load(file)
                raw_tasks = raw_data["tasks"]
                return {raw_task["name"]: TaskSchema(**raw_task) for raw_task in raw_tasks}
        except Exception as e:
            logger.error("Error while parsing tasks.yaml")
            raise
