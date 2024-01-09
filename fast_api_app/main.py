from fastapi import FastAPI
from items_views import router as items_router
from users.views import router as users_router
import uvicorn

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


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
