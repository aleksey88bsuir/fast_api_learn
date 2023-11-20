from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from pydantic import EmailStr
import uvicorn


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


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


@app.get('/items/')
def list_items():
    return [
        'item1',
        'item2',
        'item3'
    ]


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None) -> dict:
    return {'item_id': item_id, 'q': q}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
