from typing import Annotated, Union
from fastapi import Path, APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/items", tags=['Items'])


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@router.get('/')
def list_items():
    return [
        'item1',
        'item2',
        'item3'
    ]


@router.get('/{item_id}')
def read_item(item_id: Annotated[int, Path(ge=1, lt=1_000_000)], q: Union[str, None] = None) -> dict:
    return {'item_id': item_id, 'q': q}


@router.put('/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}
