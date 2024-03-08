import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload, selectinload
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
    statemant = select(User).options(joinedload(User.profile)).order_by(User.id)
    users = await session.scalars(statemant)
    for user in users:
        print(user)
        print(user.profile and user.profile.first_name)
    return list(users)


async def create_posts(session: AsyncSession, user_id: int,
                       *posts_titles: str) -> list[Post]:
    posts = [Post(title=title, user_id=user_id) for title in posts_titles]
    session.add_all(posts)
    await session.commit()
    print(posts)
    return posts


async def get_users_with_posts(session: AsyncSession) -> None:
    statement = select(User).options(joinedload(User.posts)).order_by(User.id)
    users = await session.scalars(statement)
    for user in users.unique():
        print("*" * 20)
        print(user)
        sorted_posts = sorted(user.posts, key=lambda post: post.id)
        for post in sorted_posts:
            print("-", post)


async def get_users_with_posts_2(session: AsyncSession) -> None:
    statement = select(User).options(selectinload(User.posts)).order_by(User.id)
    result: Result = await session.execute(statement)
    users = result.scalars()
    for user in users:
        print("*" * 20)
        print(user)
        sorted_posts = sorted(user.posts, key=lambda post: post.id)
        for post in sorted_posts:
            print("-", post)


async def get_posts_with_author(session: AsyncSession) -> None:
    statement = select(Post).options(joinedload(Post.user)).order_by(Post.id)
    posts = await session.scalars(statement)
    for post in posts:
        print(f'post_id: {post.id}, post: {post}, author: {post.user}')


async def get_users_with_posts_and_profiles(session: AsyncSession):
    statement = select(User).options(
        joinedload(User.profile), selectinload(User.posts)
    ).order_by(User.id)
    users = await session.scalars(statement)
    for user in users:
        print("*" * 20)
        print(user, user.profile and user.profile.first_name)
        sorted_posts = sorted(user.posts, key=lambda post: post.id)
        for post in sorted_posts:
            print("-", post)


async def get_profiles_with_users_and_users_with_posts(session: AsyncSession):
    statement = (
        select(Profile).
        join(Profile.user).
        options(joinedload(Profile.user).selectinload(User.posts)).
        where(User.name == "Alex")
        .order_by(Profile.user_id)
    )
    profiles = await session.scalars(statement)
    for profile in profiles:
        print(profile.user, profile.id and profile.first_name)
        sorted_posts = sorted(profile.user.posts, key=lambda post: post.id)
        for post in sorted_posts:
            print("-", post)


async def main():
    async with db_helper.session_factory() as session:
        # await create_user(session=session, username='Mike')
        # await create_user(session=session, username='Alex')
        # print(await read_all_users(session=session))
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
        # await show_users_with_profiles(session=session)
        # await create_posts(session, user_mike.id, "WWW", "CCC")
        # await create_posts(session, user_alex.id, "Python", "C++", "Another language")
        # await get_users_with_posts_2(session=session)
        # await get_posts_with_author(session=session)
        # await get_users_with_posts_and_profiles(session=session)
        await get_profiles_with_users_and_users_with_posts(session=session)


if __name__ == "__main__":
    asyncio.run(main())
