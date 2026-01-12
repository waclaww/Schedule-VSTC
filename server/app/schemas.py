from pydantic import BaseModel, StringConstraints
from datetime import datetime

class VStechnicalInput_schema(BaseModel):
    date: str
    schedule: str
    
from typing import Annotated


class groupNameRequest_schema(BaseModel):
    group_name: Annotated[str, StringConstraints(pattern=r"^[А-Я]{1,3}-\d{2,3}$")]
    
class VstechnicalArchive_schema(BaseModel):
    date: datetime
    schedule: str

