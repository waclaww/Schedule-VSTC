import sqlite3

connection = sqlite3.connect("./tgbot.db", check_same_thread=False)
cursor = connection.cursor()

# cursor.execute("ALTER TABLE users ADD COLUMN schedule_msg_id INTEGER;")
# connection.commit()


#Почистить бд и проверить правильность работы бота (написано влоть до отправки навзания группы в бд)