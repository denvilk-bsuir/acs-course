from repository.stats import StatRepository
from services.stats import StatsService


def stats_service() -> StatsService:
    return StatsService(StatRepository)
