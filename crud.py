import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from fast_api_app.core.models import db_helper, User, Profile, Post


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(name=username)
    session.add(user)
    await session.commit()
    return user


async def read_all_users(session: AsyncSession) -> list[User | None]:
    statement = select(User).order_by(User.id)
    result: Result = await session.execute(statement)
    users = result.scalars().all()
    return list(users)


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    statement = select(User).where(User.name == username)
    result: Result = await session.execute(statement)
    user: User | None = result.scalar_one_or_none()
    print('found user', username, user)
    return user


async def create_user_profile(
        session: AsyncSession,
        user_id: int,
        first_name: str | None = None,
        last_name: str | None = None) -> Profile:
    profile = Profile(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
    )
    session.add(profile)
    await session.commit()
    return profile


async def show_users_with_profiles(session: AsyncSession) -> list[User]:
    statemant = select(User).order_by(User.id)
    users = await session.scalars(statemant)
    for user in users:
        print(user)


async def main():
    async with db_helper.session_factory() as session:
        # await create_user(session=session, username='Mike')
        # await create_user(session=session, username='Alex')
        print(await read_all_users(session=session))
        # user_mike = await get_user_by_username(session=session, username='Mike')
        # user_alex = await get_user_by_username(session=session, username="Alex")
        # await create_user_profile(session=session,
        #                           user_id=user_alex.id,
        #                           first_name="Alex",
        #                           )
        # await create_user_profile(session=session,
        #                           user_id=user_mike.id,
        #                           first_name="Mihail",
        #                           last_name="Ivanovich"
        #                           )


if __name__ == "__main__":
    asyncio.run(main())
