from pydantic import BaseModel,ConfigDict
from datetime import datetime

class MetricOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    cpu_percentage: float
    ram_percentage: float
    time_stamp: datetime