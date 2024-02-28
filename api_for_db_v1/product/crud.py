from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select
from fast_api_app.core.models import Product

from .schemas import ProductCreate, ProductUpdate, ProductUpdatePartial


async def get_products(session: AsyncSession) -> list[Product]:
    statement = select(Product).order_by(Product.id)
    result: Result = await session.execute(statement)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def update_product(session: AsyncSession,
                         product: Product,
                         product_update: ProductUpdate) -> Product:
    for name, value in product_update.model_dump().items():
        setattr(product, name, value)
    print(product)
    await session.commit()
    return product


async def update_product_partial(session: AsyncSession,
                                 product: Product,
                                 product_update_partial: ProductUpdatePartial) -> Product:
    for name, value in product_update_partial.model_dump(exclude_unset=True).items():
        setattr(product, name, value)
        await session.commit()
        return product


async def delete_product(session: AsyncSession,
                         product: Product) -> None:
    if product:
        await session.delete(product)
        await session.commit()
