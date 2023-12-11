from .chemas import CreateUser


def create_new_user(input_data_user: CreateUser) -> dict:
    user = input_data_user.model_dump()
    return {
        'success': True,
        'new_user': user,
    }
