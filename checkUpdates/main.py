from queries import insert_query, get_query, update_query, get_archive_query
from private import *
from parse import getScheduleVSTS, isGroupName, scheduleVSTCTodayTommorrow, scheduleVSTCtoJSON, toDateTime
from schemas import VStechnicalInput
from datetime import date, now
import time
import json
import os
import telebot
import time



bot = telebot.TeleBot(bot_token)


def forCurrentSchedule():
    #Проверка страницы с рассписанием на сегодня
    todayPage = str(scheduleVSTCtoJSON(vstcToday))
    oldTodayPage = get_query()[0]['schedule']
    
    if oldTodayPage != todayPage:
        update_query(VStechnicalInput(date="today", schedule = todayPage))
        print("Обновление страницы на сегодня")
        bot.send_message(chat_id, "Обновление страницы на сегодня")
    else:
        print("Обновлений на сегодня получено не было")
        bot.send_message(chat_id, "Обновлений на сегодня получено не было")
    
    tomorrowPage = str(scheduleVSTCtoJSON(vstcTomorrow))
    oldTomorrowPage = get_query()[1]['schedule']
    if oldTomorrowPage != tomorrowPage:
        update_query(VStechnicalInput(date="tomorrow", schedule = tomorrowPage))
        print("Обновление страницы на завтра")
        bot.send_message(chat_id, "Обновление страницы на завтра")
    else:
        print("Обновлений на завтра получено не было")
        bot.send_message(chat_id, "Обновлений на завтра получено не было")

def forArchive():
    current_schedule = scheduleVSTCtoJSON(vstcTomorrow)
    current_date = date.today()
    archive_schedule = get_archive_query()
    
    if current_date == toDateTime(current_schedule['date']) and archive_schedule:
        pass
    

def check_updates():
    """
    Скрипт ожидающий обновление страницы (пока что УО"ВГТК")
    """
    while 1:
        forCurrentSchedule()
        forArchive()
        time.sleep(1800)
        
if __name__ == "__main__":
    check_updates()
