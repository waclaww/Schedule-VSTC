from fastapi import FastAPI
from .models.router import router
import uvicorn
<<<<<<< HEAD
from helpers import generate_random_string
from app.models.models import Codes, Users
from app.database import async_session_maker
from sqlalchemy import select, insert, update, delete
from .schemas import generateCode
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query 
 
app = FastAPI()

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
            }
    
        
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # или ["*"] для всех доменов
    allow_credentials=True,
    allow_methods=["*"],  # разрешает OPTIONS, POST и другие методы
    allow_headers=["*"],
)   
    
    
@app.post("/generate_code")
async def generate_code(request: generateCode):
    """Генерация рандомного кода и отправка его в БД"""
    async with async_session_maker() as session:
        code = generate_random_string(6)
        
        chat_id = request.chat_id  # 👈 Оставляем как int, НЕ конвертируем в строку
        
        query = select(Codes).where(Codes.chat_id == chat_id)  # Сравниваем int с int
        result = await session.execute(query)
        old_code = result.scalars().first()
        
        if old_code:
            query = update(Codes).where(Codes.chat_id == chat_id).values(code=code)
        else:
            query = insert(Codes).values(code=code, chat_id=chat_id)  # 👈 Передаем int
        
        await session.execute(query)
        await session.commit()
    
    return {"code": code}

@app.get("/get_all_codes")
async def get_all_codes():
    async with async_session_maker() as session:
        query = select(Codes)
        result = await session.execute(query)
        codes = result.scalars().all()
        return codes  




@app.post("/get_chat_id")
async def get_code(request: str):  
    async with async_session_maker() as session:
        query = select(Codes.chat_id).where(Codes.code == request)
        result = await session.execute(query)
        if result:
            return {"chat_id": result.scalars().first()}
        return {"chat_id": None} 
    


@app.post("/add_user")
async def add_user(chat_id: int):
    async with async_session_maker() as session:
        query = select(Codes.chat_id).where(Codes.chat_id == chat_id)
        result = await session.execute(query)
        if result:
            data = result.scalars().first()
            if data == chat_id:
                
                query = delete(Codes).where(Codes.chat_id == chat_id)
                await session.execute(query)
                session.commit()
                
                query = select(Users).where(Users.chat_id == chat_id)
                result = await session.execute(query)
                user = result.scalars().first() if result else None
                
                if user:
                    return "User already exists"
                
                else:
                    query = insert(Users).values(chat_id = chat_id, group_name = "")
                    await session.execute(query)
                    session.commit
                    return "User created"
            else:
                return "Пользователя нет"        
        

=======
 
app = FastAPI()

>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
app.include_router(router)













