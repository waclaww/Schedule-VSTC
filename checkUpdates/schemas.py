from pydantic import BaseModel
from datetime import date

class VStechnicalInput(BaseModel):
    date: str
    schedule: str
    
    
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
    

    
