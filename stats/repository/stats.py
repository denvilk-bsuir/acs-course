from models.models import Stat
from core.repository import SQLAlchemyRepository


class StatRepository(SQLAlchemyRepository):
    model = Stat
