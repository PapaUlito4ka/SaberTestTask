from fastapi import FastAPI, Depends

from configs.builds_data import lifespan
from configs.env import get_environment_variables
from metadata.tags import TAGS
from routers.v1.task_router import task_router


env = get_environment_variables()

app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=TAGS,
    lifespan=lifespan
)

app.include_router(task_router, prefix='/api')
