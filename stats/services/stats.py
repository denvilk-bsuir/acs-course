from typing import List
from core.repository import AbstractRepository
from models.schemas import StatSchema, StatBaseSchema


class StatsService:
    def __init__(self, stats_repo: AbstractRepository):
        self.stats_repo: AbstractRepository = stats_repo()

    async def add_stat(self, stat: StatBaseSchema) -> int:
        stat_dict = stat.dict()
        stat_id = await self.stats_repo.add_one(stat_dict)
        return stat_id

    async def get_stats(self) -> List[StatSchema]:
        stats = await self.stats_repo.find_all()
        return stats
    
    async def get_stat(self, id) -> StatSchema:
        stat = await self.stats_repo.find_one_by_id(id)
        return stat
