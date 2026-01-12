import requests
from bs4 import BeautifulSoup
from private import *
from datetime import date


def getScheduleVSTS(url):
    """
    Получение рассписания ВГТК(Лазо)
    """
    page = requests.get(url)
    page.encoding = 'utf-8'

    
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')

    matrix = []
    y = 0

    for row in rows:
        cells = row.find_all('td')
        x = 0

        for cell in cells:
            rowspan = int(cell.get('rowspan', 1))
            colspan = int(cell.get('colspan', 1))

            while y < len(matrix) and x < len(matrix[y]) and matrix[y][x]:
                x += 1
            for dy in range(rowspan):
                rowY = y + dy
                while len(matrix) <= rowY:
                    matrix.append([])
                while len(matrix[rowY]) <= x + colspan - 1:
                    matrix[rowY].append(None)

                for dx in range(colspan):
                    matrix[rowY][x + dx] = cell

            x += colspan
        y += 1
    return matrix


def isGroupName(text):
    """
    Проверка, является ли строка названием группы
    """
    if not text:
        return False
    text = text.strip()
    if '-' in text and text.split('-')[1].isdigit():
        return True
    

import json

def scheduleVSTCtoJSON(url):
    """
    Получение расписания ВГТК(Лазо) в корректном JSON
    """
    matrix = getScheduleVSTS(url)
    schedule = []
    groups = {}

    # преобразуем таблицу в список строк
    for row in matrix:
        schedule_row = []
        for cell in row:
            if cell:
                schedule_row.append(cell.get_text(strip=True))
            else:
                schedule_row.append(None)
        schedule.append(schedule_row)

    # первая ячейка — дата
    groups["date"] = schedule[0][0]

    # ищем названия групп
    for row in range(len(schedule)):
        for col in range(len(schedule[row])):
            if isGroupName(schedule[row][col]):
                times, lessons, rooms = [], [], []
                for i in range(12):
                    times.append(schedule[row + i][1])
                    lessons.append(schedule[row + i][col])
                    rooms.append(schedule[row + i][col + 1])
                groups[schedule[row][col]] = f"{[times, lessons, rooms]}"

    return json.dumps(groups, ensure_ascii=False, indent=2)


def scheduleVSTCTodayTommorrow():
    """
    Получение рассписания ВГТК(Лазо) на сегодня и на завтра одновременно, в формате JSON
    """
    return {"today": scheduleVSTCtoJSON(vstcToday), "tomorrow": scheduleVSTCtoJSON(vstcToday)}


def toDateTime(date_string: str):
    """Преобразовывание даты с сайта УО 'ВГТК' в 'YYYY-MM-DD' формат"""
    months = {
        'янв': '01',
        'фев': '02',
        'мар': '03',
        'апр': '04',
        'мая': '05',
        'июн': '06',
        'июл': '07',
        'авг': '08',
        'сен': '09',
        'окт': '10',
        'ноя': '11',
        'дек': '12',
    }
    date_string = date_string.split()
    
    if date_string[0] == 'с':
        year = date_string[5]
        
        month = months[date_string[4][0:3]]
        
        days = []
        for day in range(int(date_string[1]), int(date_string[3])+1):
            days.append(day)
            
        current_day = date.today().day
        if current_day in days:
            return f"{year}-{month}-{current_day}"
        
        
    
    elif date_string[0] == 'на':
        """Надо будет дописать"""
        pass
# print(toDateTime("с 12 по 16 января 2026  года"))