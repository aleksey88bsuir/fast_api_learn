from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fast_api_app.core.models import db_helper
from . import crud
from .dependencies import get_product_by_id
from .schemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial


router = APIRouter(tags=["Product"])


@router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.scope_session_dependency)):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(product_in: ProductCreate,
                         session: AsyncSession = Depends(db_helper.scope_session_dependency)
                         ):
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
async def get_product(product: Product = Depends(get_product_by_id)):
    return product


@router.put('/{product_id}/')
async def update_product(
        product_update: ProductUpdate,
        product: Product = Depends(get_product_by_id),
        session: AsyncSession = Depends(db_helper.scope_session_dependency)
        ):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.patch('/{product_id}/')
async def update_product_partial(
        product_update: ProductUpdatePartial,
        product: Product = Depends(get_product_by_id),
        session: AsyncSession = Depends(db_helper.scope_session_dependency)
        ):
    return await crud.update_product_partial(
        session=session,
        product=product,
        product_update_partial=product_update,
        partial=True,
    )
