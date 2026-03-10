from pydantic import BaseModel, StringConstraints

class VStechnicalInput(BaseModel):
    date: str
    schedule: str
    
from typing import Annotated


class groupNameRequest(BaseModel):
    group_name: Annotated[str, StringConstraints(pattern=r"^[А-Я]{1,3}-\d{2,3}$")]
