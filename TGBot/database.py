import sqlite3

connection = sqlite3.connect("./tgbot.db", check_same_thread=False)
cursor = connection.cursor()

<<<<<<< HEAD
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
=======
# cursor.execute("ALTER TABLE users ADD COLUMN schedule_msg_id INTEGER;")
# connection.commit()

>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8

#Почистить бд и проверить правильность работы бота (написано влоть до отправки навзания группы в бд)