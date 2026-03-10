import telebot
from telebot import types
from private import bot
from database import connection, cursor
from helpers import *
<<<<<<< HEAD
from keyboards import *
from json.decoder import JSONDecodeError
from datetime import datetime
from zoneinfo import ZoneInfo


#КНОПКИ
=======

#КНОПКИ
schedule = types.InlineKeyboardMarkup(row_width=1)
kb = types.InlineKeyboardButton
schedule.add(
    kb(text="На сегодня", callback_data="today"),
    kb(text="На завтра", callback_data="tomorrow"),
    kb(text="Сменить группу", callback_data="change_group")
)
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8


#СТАРТ БОТА
@bot.message_handler(commands=['start'])
def start(message):
<<<<<<< HEAD
    bot.delete_message(message.chat.id, message.message_id)
    cursor.execute("SELECT * FROM users WHERE chat_id = ?", [message.chat.id])
    user = cursor.fetchone()
    
    if user and user[3]:  # group_name
        try:
            data = get_schedule(user[3], "tomorrow")
            
            # Всегда отправляем новое сообщение при очистке истории
            # так как старые сообщения удалены
            try:
                # Пробуем удалить старое сообщение, если оно существует
                cursor.execute("SELECT schedule_msg_id FROM users WHERE chat_id = ?", [message.chat.id])
                old_msg_id = cursor.fetchone()[0]
                try:
                    bot.delete_message(message.chat.id, old_msg_id)
                except:
                    pass  # сообщение уже удалено или не существует
            except:
                pass
            
            # Отправляем новое сообщение
            sent = bot.send_message(
                message.chat.id,
                viewSchedule(data),
                reply_markup=fullSchedule,
                parse_mode="HTML"
            )
            
            # Обновляем ID нового сообщения в базе
            cursor.execute("UPDATE users SET schedule_msg_id = ? WHERE chat_id = ?", 
                         [sent.message_id, message.chat.id])
            connection.commit()
            
        except KeyError:
            cursor.execute("SELECT schedule_msg_id FROM users WHERE chat_id = ?", [message.chat.id])
            msg_id = cursor.fetchone()
            
            try: 
                msg_id = msg_id[0]
                cursor.execute("UPDATE users SET step = ? WHERE chat_id = ?", ["change_group", message.chat.id])
                connection.commit()
                bot.edit_message_text(
                    chat_id=message.chat.id, 
                    message_id=msg_id,
                    text="К сожалению такой группы в колледже нет. <b>Попробуйте снова!</b>⚠️",
                    parse_mode="HTML",
                )
            except telebot.apihelper.ApiTelegramException:
                msg_id = bot.send_message(
                    chat_id=message.chat.id,
                    text="Введите название новой группы.✍️",
                    parse_mode="HTML",
                ).message_id  
                cursor.execute("UPDATE users SET step = ?, schedule_msg_id = ? WHERE chat_id = ?", 
                             ["change_group", msg_id, message.chat.id])
                connection.commit()
                
    else:
        msg_id = bot.send_message(message.chat.id, f"Здравствуйте, @{message.from_user.username}! Этот бот создан для удобного просмотра расписания учебных занятий ВГТК. Введите название вашей учебной группы.").message_id
        cursor.execute("INSERT INTO users (chat_id, username, step, schedule_msg_id) VALUES (?, ?, ?, ?)", 
                      [message.chat.id, message.from_user.username, "change_group", msg_id])
        connection.commit()

@bot.message_handler(commands=['auth_in_app'])
def auth_in_app(message):
    bot.delete_message(message.chat.id, message.message_id)
    
    bot.send_message(
        message.chat.id, 
        f"У нас есть мобильное веб-приложение📱. Зайдите в 🌐<a href=\"https://schedule-vstc-pwa.vercel.app/\">приложение</a> и введите этот код <code>{generate_code(message.chat.id)}</code>, чтобы просматривать расписание стало еще удобнее для вас!😊", 
        parse_mode="HTML",
    )
    
=======
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


>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
#ТЕКСТОВЫЕ СООБЩЕНИЯ
@bot.message_handler(content_types=['text'])
def main(message):
    mci, text = message.chat.id, message.text
<<<<<<< HEAD
    
    cursor.execute("SELECT step FROM users WHERE chat_id = ?", [mci])
    step = cursor.fetchone()
    if step: step = step[0]
    print(step)
    
    cursor.execute("SELECT schedule_msg_id FROM users WHERE chat_id = ?", [mci])
    msg_id = cursor.fetchone()
    if msg_id: msg_id = msg_id[0]
    
    if step == "change_group":
        try:
            group_name = text.upper()
            data = get_schedule(group_name, "tomorrow")
            print(data)
            cursor.execute("UPDATE users SET group_name = ?, step = ? WHERE chat_id = ?", [group_name, "get_group", mci])
            connection.commit()
            bot.edit_message_text(
                chat_id=mci,
                message_id=msg_id,
                text=viewSchedule(get_schedule(text.upper(), 'tomorrow')),
                reply_markup=todaySchedule,
                parse_mode="HTML"
            )
        except KeyError or JSONDecodeError:
            bot.delete_message(mci, message.message_id)
            
            bot.edit_message_text(
                chat_id=mci,
                message_id=msg_id,
                text="К сожалению такой группы в колледже нет. <b>Попробуйте снова!</b>⚠️",
                parse_mode="HTML",
            )
            cursor.execute("UPDATE users SET step = 'change_group' WHERE chat_id = ?", [mci])
            
            
    elif step == "get_group":
        bot.delete_message(mci, message.message_id)
        bot.edit_message_text(
            chat_id=mci,
            message_id=msg_id,
            text=viewSchedule(get_schedule(text.upper(), 'tomorrow')),
            reply_markup=tomorrowSchedule,
            parse_mode="HTML"
        )
            

        cursor.execute("SELECT group_name, schedule_msg_id FROM users WHERE chat_id = ?", [mci])
        data = cursor.fetchone()
        if data and data[0]:
            try:
                bot.edit_message_text(
                    chat_id=mci,
                    message_id=msg_id[1],
                    text=viewSchedule(data[0]),
                    reply_markup=tomorrowSchedule,
                    parse_mode="HTML"
=======
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
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
                )
            except telebot.apihelper.ApiTelegramException as e:
                if "message is not modified" in str(e):
                    pass  # игнорируем
                else:
                    raise
        else:
<<<<<<< HEAD
            pass
            sent = bot.send_message(mci, viewSchedule(data), reply_markup=fullSchedule)
=======
            sent = bot.send_message(mci, viewSchedule(data), reply_markup=schedule)
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
            cursor.execute("UPDATE users SET schedule_msg_id = ? WHERE chat_id = ?", [sent.message_id, mci])
            connection.commit()
    bot.delete_message(mci, message.message_id)

<<<<<<< HEAD

=======
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
#ОБРАБОТЧИК КНОПОК
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    mci = call.message.chat.id
    bot.answer_callback_query(call.id)

    if call.data in ("today", "tomorrow"):
        cursor.execute("SELECT group_name, schedule_msg_id FROM users WHERE chat_id = ?", [mci])
        row = cursor.fetchone()
<<<<<<< HEAD
        if row:
            group_name, msg_id = row[0], row[1]
            data = get_schedule(group_name, call.data)

            new_text = viewSchedule(data)
            old_text = call.message.text

            new_markup = get_schedule_keyboard(call.data)
                
            old_markup = call.message.reply_markup
            
            cursor.execute("UPDATE users SET viewing = ? WHERE chat_id = ?", [call.data, call.message.chat.id])
            connection.commit()

            if new_text != old_text or markup_to_json(new_markup) != markup_to_json(old_markup):
                try:
                    bot.edit_message_text(
                        chat_id=mci,
                        message_id=msg_id,
                        text=new_text,
                        reply_markup=new_markup,
                        parse_mode="HTML"
                    )
                except telebot.apihelper.ApiTelegramException as e:
                    if "message is not modified" in str(e):
                        pass
                    else:
                        raise
            else:
                bot.answer_callback_query(call.id, text="Расписание не изменилось")
        else:
            bot.send_message(
                call.message.chat.id, 
                "К сожалению у нас возникли неполадки, чтобы продолжить использование <b>вам нужно нажать на кнопку \"Сменить группу\"</b>. Просим прощение за неудобство!",
                parse_mode="HTML"
            )
                             

    elif call.data == "change_group":
        cursor.execute("SELECT group_name FROM users WHERE chat_id = ?", [call.message.chat.id])
        user = cursor.fetchone()
        if user:
            cursor.execute("UPDATE users SET step = 'change_group' WHERE chat_id = ?", [mci])
            connection.commit()
            cursor.execute("SELECT schedule_msg_id FROM users WHERE chat_id = ?", [mci])
            msg_id = cursor.fetchone()[0]
=======
        group_name, msg_id = row[0], row[1]
        data = get_schedule(group_name, call.data)

        new_text = viewSchedule(data)
        old_text = call.message.text

        new_markup = schedule
        old_markup = call.message.reply_markup

        if new_text != old_text or markup_to_json(new_markup) != markup_to_json(old_markup):
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
            try:
                bot.edit_message_text(
                    chat_id=mci,
                    message_id=msg_id,
<<<<<<< HEAD
                    text="Введите название новой группы.✍️"
=======
                    text=new_text,
                    reply_markup=new_markup
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
                )
            except telebot.apihelper.ApiTelegramException as e:
                if "message is not modified" in str(e):
                    pass
                else:
                    raise
        else:
<<<<<<< HEAD
            bot.delete_message(call.message.chat.id, call.message.message_id)
            mes_id = bot.send_message(call.message.chat.id, "Введите название новой группы.✍️").message_id
            cursor.execute("INSERT INTO users (chat_id, group_name, step, schedule_msg_id) VALUES (?, ?, ?, ?)", [call.message.chat.id,  call.message.text, "change_group", mes_id])
            connection.commit()
            
    elif call.data == "update":
        cursor.execute("SELECT group_name, schedule_msg_id, viewing FROM users WHERE chat_id = ?", [call.message.chat.id])
        data = cursor.fetchone()
        if data: 
            group_name = data[0]
            msg_id = data[1]
            viewing = data[2]
            print(viewing)
            try:
                
                
                bot.edit_message_text(
                    chat_id=call.message.chat.id, 
                    message_id=msg_id,
                    text=f"{viewSchedule(get_schedule(group_name, viewing))}\n<b>Обновлено <i>{datetime.now(ZoneInfo("Europe/Moscow")).strftime("%H:%M:%S")} PM</i></b>",
                    reply_markup=get_schedule_keyboard(viewing),
                    parse_mode="HTML"
                )
            except telebot.apihelper.ApiTelegramException as e:
                if "message is not modified" in str(e):
                    pass
                else:
                    raise
        

print("Бот запущен...")
bot.polling(none_stop=True)
=======
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
>>>>>>> 72d1659d962418f5667d3a9f3ee0be9af88fd7b8
