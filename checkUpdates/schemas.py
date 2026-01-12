from pydantic import BaseModel
from datetime import datetime

class VStechnicalInput(BaseModel):
    date: str
    schedule: str
    
    
class VstechnicalArchive(BaseModel):
    date: datetime
    schedule: str
    

    
