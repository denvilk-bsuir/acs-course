import datetime
from pydantic import BaseModel


class StatBaseSchema(BaseModel):
    destination: str
    created_at: datetime.datetime

class StatSchema(StatBaseSchema):
    id: int
