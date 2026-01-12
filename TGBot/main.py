import telebot
from telebot import types
from private import bot
from database import connection, cursor
from helpers import *

#КНОПКИ
schedule = types.InlineKeyboardMarkup(row_width=1)
kb = types.InlineKeyboardButton
schedule.add(
    kb(text="На сегодня", callback_data="today"),
    kb(text="На завтра", callback_data="tomorrow"),
    kb(text="Сменить группу", callback_data="change_group")
)


#СТАРТ БОТА
@bot.message_handler(commands=['start'])
def start(message):
    cursor.execute("SELECT * FROM users WHERE chat_id = ?", [message.chat.id])
    user = cursor.fetchone()
    if user:
        if user[3]:  # group_name
            data = get_schedule(user[3], "today")
            sent = bot.send_message(
                message.chat.id,
                viewSchedule(data),
                reply_markup=schedule
            )
            cursor.execute("UPDATE users SET schedule_msg_id = ? WHERE chat_id = ?", [sent.message_id, message.chat.id])
            connection.commit()
        else:
            cursor.execute("UPDATE users SET step = ? WHERE chat_id = ?", ["get_group", message.chat.id])
            connection.commit()
            bot.send_message(message.chat.id, f"Здравствуйте, @{message.from_user.username}, введите название вашей учебной группы.")
    else:
        cursor.execute("INSERT INTO users (chat_id, step) VALUES (?, ?)", [message.chat.id, "get_group"])
        connection.commit()
        bot.send_message(message.chat.id, f"Здравствуйте, @{message.from_user.username}! Этот бот создан для удобного просмотра расписания учебных занятий ВГТК. Введите название вашей учебной группы.")


#ТЕКСТОВЫЕ СООБЩЕНИЯ
@bot.message_handler(content_types=['text'])
def main(message):
    mci, text = message.chat.id, message.text
    cursor.execute("SELECT step FROM users WHERE chat_id = ?", [mci])
    step = cursor.fetchone()
    if step: step = step[0]

    if step in ("get_group", "change_group"):
        group_name = text.upper()
        cursor.execute("UPDATE users SET group_name = ?, step = ? WHERE chat_id = ?", [group_name, None, mci])
        connection.commit()
        data = get_schedule(group_name, "today")

        cursor.execute("SELECT schedule_msg_id FROM users WHERE chat_id = ?", [mci])
        msg_id = cursor.fetchone()
        if msg_id and msg_id[0]:
            try:
                bot.edit_message_text(
                    chat_id=mci,
                    message_id=msg_id[0],
                    text=viewSchedule(data),
                    reply_markup=schedule
                )
            except telebot.apihelper.ApiTelegramException as e:
                if "message is not modified" in str(e):
                    pass  # игнорируем
                else:
                    raise
        else:
            sent = bot.send_message(mci, viewSchedule(data), reply_markup=schedule)
            cursor.execute("UPDATE users SET schedule_msg_id = ? WHERE chat_id = ?", [sent.message_id, mci])
            connection.commit()
    bot.delete_message(mci, message.message_id)

#ОБРАБОТЧИК КНОПОК
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    mci = call.message.chat.id
    bot.answer_callback_query(call.id)

    if call.data in ("today", "tomorrow"):
        cursor.execute("SELECT group_name, schedule_msg_id FROM users WHERE chat_id = ?", [mci])
        row = cursor.fetchone()
        group_name, msg_id = row[0], row[1]
        data = get_schedule(group_name, call.data)

        new_text = viewSchedule(data)
        old_text = call.message.text

        new_markup = schedule
        old_markup = call.message.reply_markup

        if new_text != old_text or markup_to_json(new_markup) != markup_to_json(old_markup):
            try:
                bot.edit_message_text(
                    chat_id=mci,
                    message_id=msg_id,
                    text=new_text,
                    reply_markup=new_markup
                )
            except telebot.apihelper.ApiTelegramException as e:
                if "message is not modified" in str(e):
                    pass
                else:
                    raise
        else:
            bot.answer_callback_query(call.id, text="Расписание не изменилось")

    elif call.data == "change_group":
        cursor.execute("UPDATE users SET step = 'change_group' WHERE chat_id = ?", [mci])
        connection.commit()
        cursor.execute("SELECT schedule_msg_id FROM users WHERE chat_id = ?", [mci])
        msg_id = cursor.fetchone()[0]
        try:
            bot.edit_message_text(
                chat_id=mci,
                message_id=msg_id,
                text="Введите название новой группы."
            )
        except telebot.apihelper.ApiTelegramException as e:
            if "message is not modified" in str(e):
                pass
            else:
                raise

print("Бот запущен...")
bot.polling(none_stop=True)
