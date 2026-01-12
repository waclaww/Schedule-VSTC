from fastapi import APIRouter, HTTPException, Request
from sqlalchemy import select, insert, update
from app.database import async_session_maker
from app.models.models import Vstechincal_data, Vstechnical_archive
from app.schemas import *
import json
from datetime import datetime

router = APIRouter(prefix="/schedule", tags=["Получение рассписания с бд"])

@router.get("/vstechnical_get", summary="Получить рассписание")
async def get_VSTechnical_schedule():
    async with async_session_maker() as session:
        query = select(Vstechincal_data)
        result = await session.execute(query)
        schedule = result.scalars().all()
        return schedule
    
@router.post("/vstechical_update/")
async def update_vstechical_schedule(data: VStechnicalInput_schema, request: Request):
    client_host = request.client.host
    if client_host not in ("127.0.0.1", "localhost"):
        raise HTTPException(status_code=403, detail="Access denied")
    else:
        async with async_session_maker() as session:
            stmt = update(Vstechincal_data).where(Vstechincal_data.date == data.date).values(schedule = data.schedule)
            await session.execute(stmt)
            await session.commit()
            return {"status": "done"}    


@router.post("/vstechical_insert/")
async def insert_vstechical_schedule(data: VStechnicalInput_schema, request: Request):
    client_host = request.client.host
    if client_host not in ("127.0.0.1", "localhost"):
        raise HTTPException(status_code=403, detail="Access denied")
    else:
        async with async_session_maker() as session:
            stmt = insert(Vstechincal_data).values(
                date=data.date,
                prepare_data=data.schedule
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": "done"}
        
@router.post("/vstechnical_archive_insert")
async def insert_vstechical_schedule(data: VstechnicalArchive_schema, request: Request):
    client_host = request.client.host
    if client_host not in ("127.0.0.1", "localhost"):
        raise HTTPException(status_code=403, detail="Access denied")
    else:
        async with async_session_maker() as session:
            stmt = insert(Vstechnical_archive).values(
                date=data.date,
                prepare_data=data.schedule
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": "done"}
        
@router.post("/vstechnical_archive_get_date")
async def insert_vstechical_schedule(data: datetime, request: Request):
    client_host = request.client.host
    if client_host not in ("127.0.0.1", "localhost"):
        raise HTTPException(status_code=403, detail="Access denied")
    else:
        async with async_session_maker() as session:
            query = select(Vstechnical_archive).where(Vstechnical_archive.date == data)
            result = await session.execute(query)
            schedule_raw = result.scalars().all()

            return {"status": "done", "schedule": schedule_raw}

    
@router.post("/vstechnical_group/")
async def get_schedule_of_group(request: groupNameRequest_schema):
    async with async_session_maker() as session:
        query = select(Vstechincal_data.schedule)
        result = await session.execute(query)
        schedule_raw = result.scalars().all()

        today_entry = json.loads(schedule_raw[0])[request.group_name]
        tomorrow_entry = json.loads(schedule_raw[1])[request.group_name] 
        
        

        return {
            "today": today_entry,
            "tomorrow": tomorrow_entry
        }