from schemas import VStechnicalInput, VstechnicalArchive
import requests
from datetime import datetime

def insert_query(data: VStechnicalInput):
    response = requests.post("http://127.0.0.1:8000/schedule/vstechical_insert/", json=data.dict())
    response.encoding = 'utf-8'
    return [response.status_code, response.json()]

def insert_archive_query(data: VstechnicalArchive):
    response = requests.post("http://127.0.0.1:8000/schedule/vstechical_archive_insert/", json=data.dict())
    response.encoding = 'utf-8'
    return [response.status_code, response.json()]

def get_query():
    response = requests.get("http://127.0.0.1:8000/schedule/vstechnical_get")
    response.encoding = 'utf-8'
    return response.json() if response else "no data"

def update_query(data: VStechnicalInput):
    response = requests.post("http://127.0.0.1:8000/schedule/vstechical_update/", json=dict(data))
    response.encoding = 'utf-8'
    return [response.status_code, response.json()]

def get_archive_query(date: datetime):
    response = requests.post("http://127.0.0.1:8000/schedule/vstechnical_archive_get_date", data=date)
    response.encoding = "utf-8"
    return response.json() if response else False