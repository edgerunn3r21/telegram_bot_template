import logging
import traceback

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


async def orm_create(session: AsyncSession, model: object, data: dict):
    try:
        obj = model(**data)
        session.add(obj)
        await session.commit()

        return True
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())

        return False


async def orm_read(session: AsyncSession, model: object, as_iterable: bool = False, **filters):
    try:
        query = select(model)
        if filters:
            query = query.filter_by(**filters)

        result = await session.execute(query)
        items = result.scalars().all()

        if len(items) == 1 and as_iterable is False:
            return items[0]

        return items
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
   
        return False


async def orm_update(session: AsyncSession, model: object, pk: int, data: dict):
    try:
        await session.execute(update(model).where(model.pk == pk).values(**data))
        return await session.commit()
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
    
        return False


async def orm_delete(session: AsyncSession, model: object, pk: int):
    try:
        await session.execute(delete(model).where(model.pk == pk))
        return await session.commit()
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
      
        return False
