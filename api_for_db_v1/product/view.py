from fastapi import APIRouter, HTTPException, status

from . import crud
from .schemas import Product, ProductCreate


router = APIRouter(tags=["Product"])


@router.get("/", response_model=list[Product])
async def get_products(session):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(session, product_in: ProductCreate):
    try:
        product = await crud.create_product(session=session, product_in=product_in)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Product not create'
        )
    if product:
        return product


@router.get('/{product_id}/', response_model=Product)
async def get_product(product_id: int, session):
    product = await crud.get_product(session=session, product_id=product_id)
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Product {product_id} not found'
    )
