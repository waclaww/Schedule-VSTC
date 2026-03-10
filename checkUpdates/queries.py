from schemas import VStechnicalInput, VstechnicalArchive
import requests
from datetime import datetime

def insert_query(data: VStechnicalInput):
<<<<<<< HEAD
    response = requests.post("http://server:8000/schedule/vstechical_insert/", json=data.dict())
=======
    response = requests.post("http://127.0.0.1:8000/schedule/vstechical_insert/", json=data.dict())
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
    response.encoding = 'utf-8'
    return [response.status_code, response.json()]

def insert_archive_query(data: VstechnicalArchive):
<<<<<<< HEAD
    response = requests.post("http://server:8000/schedule/vstechnical_archive_insert/", json=data.dict())
=======
    response = requests.post("http://127.0.0.1:8000/schedule/vstechical_archive_insert/", json=data.dict())
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
    response.encoding = 'utf-8'
    return [response.status_code, response.json()]

def get_query():
<<<<<<< HEAD
    response = requests.get("http://server:8000/schedule/vstechnical_get")
=======
    response = requests.get("http://127.0.0.1:8000/schedule/vstechnical_get")
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
    response.encoding = 'utf-8'
    return response.json() if response else "no data"

def update_query(data: VStechnicalInput):
<<<<<<< HEAD
    response = requests.post("http://server:8000/schedule/vstechical_update/", json=dict(data))
=======
    response = requests.post("http://127.0.0.1:8000/schedule/vstechical_update/", json=dict(data))
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
    response.encoding = 'utf-8'
    return [response.status_code, response.json()]

def get_archive_query(date: datetime):
<<<<<<< HEAD
    response = requests.post("http://server:8000/schedule/vstechnical_archive_get_date", data=date)
    response.encoding = "utf-8"
    return response.json() if response else False

=======
    response = requests.post("http://127.0.0.1:8000/schedule/vstechnical_archive_get_date", data=date)
    response.encoding = "utf-8"
    return response.json() if response else False
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
