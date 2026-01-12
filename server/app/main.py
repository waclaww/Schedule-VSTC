from fastapi import FastAPI
from .models.router import router
import uvicorn
 
app = FastAPI()

app.include_router(router)













