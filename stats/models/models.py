from sqlalchemy import Column, Integer, String, DateTime
from models.schemas import StatSchema
from core.database import Base


class Stat(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True)
    destination = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True))

    def to_read_model(self) -> StatSchema:
        return StatSchema(
            id=self.id,
            destination=self.destination,
            created_at=self.created_at,
        )
