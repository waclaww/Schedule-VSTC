import requests
import json
import ast
<<<<<<< HEAD
from datetime import date as dt
=======
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8


def get_schedule(group_name: str, day: str = "today"):
    response = requests.post(
<<<<<<< HEAD
        "http://server:8000/schedule/vstechnical_group/",
=======
        "http://127.0.0.1:8000/schedule/vstechnical_group/",
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
        json={"group_name": group_name}
    )
    raw = json.loads(response.content)[day]
    return ast.literal_eval(raw)


<<<<<<< HEAD
def transformDate(date: str):
    
    weekDays = {
        1: "понедельник",
        1: "вторник",
        2: "среда",
        3: "четверг",
        4: "пятница",
        5: "суббота",
        6: "воскресенье",
                }
    
    date = date.split()
    
    if date[0] == "на":
        return f"{date[-1].replace('(', '').replace(')', '').capitalize()}, <u>{date[1]} {date[2]}</u>"
        
    
    elif date[0] == "с":
        year = date[5]
        
        month = date[4]
        
        days = []
        for day in range(int(date[1]), int(date[3])+1):
            days.append(day)
            
        current_day = dt.today().day
        if current_day in days:
            
            return f"<u>{current_day} {month}</u> {weekDays[dt.today().weekday().lower()]}"
    
    

print(transformDate("на 7 февраля 2025 года (ПОНЕДЕЛЬНИК)"))


def viewSchedule(data: list):
    text = f"<b>📋 Расписание группы <u>{data[1][0]}</u></b>\n"
    text += f"\n<b>📅 {transformDate(data[3])}</b>\n"
    
    
    
    # while data[1] and data[1][-1] == '':
    #     data[1].pop()
        
    for i in range(0, len(data[0])):
        data[0][i] = data[0][i].replace('–', '-').replace(' ', '')
        
    times, lessons, rooms = [], [], []
    length = len(data[1]) - 1
    indexes = []
    
    for i in range(length):
        if i + 1 <= length and data[1][i] == data[1][i+1] and data[2][i] == data[2][i+1] and data[0][i] != "DELETE":
            time = f"{data[0][i].split('-')[0]}-{data[0][i+1].split('-')[1]}"
            data[0][i+1] = "DELETE"
            times.append(time)
            
            lessons.append(data[1][i])
            
            rooms.append(data[2][i])
        
        elif data[0][i] == "DELETE":
            pass    
        
        else:
            times.append(data[0][i])
            lessons.append(data[1][i])
            rooms.append(data[2][i])
            
            
            
            
    for i in range(1, len(times)):
        if lessons[i] != "":
            text += f"\n{times[i]} <b>|</b> {lessons[i]} {rooms[i]}\n"
=======
def viewSchedule(data: list):
    print(data)
    text = f"Расписание учебной группы {data[1][0]}:\n"
    prev_time, prev_lesson = None, None  
    for i in range(1, len(data[0])):
        if data[1] != "":
            text += f"\n{data[0][i]} \"{data[1][i]} : {data[2][i]}\"\n"
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
    return text


def markup_to_json(markup):
    return json.dumps(markup.to_dict(), sort_keys=True)
<<<<<<< HEAD

def user_auth():
    return False

def generate_code(chat_id: int) -> str:
    response = requests.post("http://server:8000/generate_code", json={"chat_id": chat_id})
    
    if response.status_code == 200:
        return response.json()['code']




=======
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
