from fastapi import FastAPI
from items_views import router as items_router
from fast_api_app.users.views import router as users_router
from api_for_db_v1 import router as api_shop_router
from contextlib import asynccontextmanager
from fast_api_app.core.settings import config
from fast_api_app.core.models import Base, db_helper
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(api_shop_router, prefix=config.api_shop_router)


@app.get('/')
def hello_index():
    return {
        'my_message': 'Hello world!'
    }


@app.get('/hello/')
def hello_name(name: str):
    name = name.strip().title()
    return {
        'my_message': f'Hello {name}'
    }


@app.post('/calc/add')
def calc(arg1: int, arg2: int):
    return {'a': arg1,
            'b': arg2,
            'result': arg1 + arg2
            }


@app.get('/species')
def hello_species():
    return {
        'my_message': 'In Canada i see many species of dogs'
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
