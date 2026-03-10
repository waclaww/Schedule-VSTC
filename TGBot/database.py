import sqlite3

connection = sqlite3.connect("./tgbot.db", check_same_thread=False)
cursor = connection.cursor()

# ИСПРАВЛЕНО: тройные кавычки для многострочного запроса
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    chat_id TEXT UNIQUE,
    username TEXT,
    group_name TEXT,
    step TEXT,
    schedule_msg_id TEXT,
    viewing TEXT DEFAULT 'tomorrow'
);""")
connection.commit()

#Почистить бд и проверить правильность работы бота (написано влоть до отправки навзания группы в бд)