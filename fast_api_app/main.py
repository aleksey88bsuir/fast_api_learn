from fastapi import FastAPI, Path
from typing import Union
from items_views import router as items_router
from pydantic import EmailStr, BaseModel
from typing import Annotated
import uvicorn


app = FastAPI()
app.include_router(items_router, prefix='/items-router')


class CreateUser(BaseModel):
    email: EmailStr


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


@app.get('/users/')
def create_users(user: CreateUser):
    return {'message': f'user successful create, user email: {user.email}'}


@app.get('/species')
def hello_species():
    return {
        'my_message': 'In Canada i see many species of dogs'
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
