from datetime import datetime
from sqlalchemy import select, func
from models.models import Stat
from core.repository import SQLAlchemyRepository
from core.database import async_session_maker


class StatRepository(SQLAlchemyRepository):
    model = Stat

    async def find_from_time(self, dt: datetime):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.created_at >= dt)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res


    async def find_last_top(self, dt: datetime):
        async with async_session_maker() as session:
            stmt = (
                select(Stat.destination, func.count(Stat.destination).label('count'))
                .where(Stat.created_at >= dt)
                .group_by(Stat.destination)
                .order_by(func.count(Stat.destination).desc())
                .limit(20)
            )
            result = await session.execute(stmt)
            return result.all()