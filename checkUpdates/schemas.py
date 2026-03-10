from pydantic import BaseModel
<<<<<<< HEAD
from datetime import date
=======
from datetime import datetime
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8

class VStechnicalInput(BaseModel):
    date: str
    schedule: str
    
    
<<<<<<< HEAD
from pydantic import BaseModel, field_validator

class VstechnicalArchive(BaseModel):
    date: str  # Храним как строку
    schedule: str
    
    @field_validator('date')
    def validate_date_format(cls, v):
        # Проверяем формат YYYY-MM-DD
        from datetime import datetime
        try:
            datetime.strptime(v, "%Y-%m-%d")
            return v
        except ValueError:
            raise ValueError('Дата должна быть в формате ГГГГ-ММ-ДД')
    
=======
class VstechnicalArchive(BaseModel):
    date: datetime
    schedule: str
    
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8

    
