from fastapi import APIRouter
from .chemas import CreateUser
from .crud import create_new_user


router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
def create_users(user: CreateUser):
    return create_new_user(input_data_user=user)
