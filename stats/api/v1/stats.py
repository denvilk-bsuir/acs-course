from fastapi import APIRouter, Depends
from models.schemas import StatBaseSchema, StatSchema
from services.stats import StatsService
from core.dependencies import stats_service

router = APIRouter(
    prefix="/api",
)


@router.post("/")
async def add_stat(
    stat: StatBaseSchema,
    stats_service: StatsService = Depends(stats_service),
):
    print(stat)
    stat_id = await stats_service.add_stat(stat)
    return {"stat_id": stat_id}


@router.get("/")
async def get_stats(
    stats_service: StatsService = Depends(stats_service),
):
    stats = await stats_service.get_stats()
    return stats

@router.get("/{stat_id:int}")
async def get_stat(
    stat_id: int,
    stats_service: StatsService = Depends(stats_service)
):
    stat = await stats_service.get_stat(stat_id)
    return stat