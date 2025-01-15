from database.models import async_session
from database.models import User
from sqlalchemy import select


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def set_shift(tg_id, shift=None):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        user.shift = shift
        await session.commit()


async def set_time(tg_id, last_seen_time=None):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        user.last_seen = last_seen_time
        await session.commit()


async def set_notes(tg_id, note_text=None):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        user.notes = note_text
        await session.commit()


async def delete_notes(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        user.notes = None
        await session.commit()


async def find_rostov_acc_1():
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User.tg_id).where(User.shift == "rostov.acc.1"))
            user_ids = result.scalars().all()
    return user_ids


async def find_rostov_acc_2():
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User.tg_id).where(User.shift == "rostov.acc.2"))
            user_ids = result.scalars().all()
    return user_ids


async def find_rostov_acc_3():
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User.tg_id).where(User.shift == "rostov.acc.3"))
            user_ids = result.scalars().all()
    return user_ids


async def find_rostov_acc_4():
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User.tg_id).where(User.shift == "rostov.acc.4"))
            user_ids = result.scalars().all()
    return user_ids


async def find_rostov_acc_5():
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User.tg_id).where(User.shift == "rostov.acc.5"))
            user_ids = result.scalars().all()
    return user_ids


async def find_rostov_acc_6():
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User.tg_id).where(User.shift == "rostov.acc.6"))
            user_ids = result.scalars().all()
    return user_ids


async def find_stavropol():
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User.tg_id).where(User.shift == "stavropol"))
            user_ids = result.scalars().all()
    return user_ids
