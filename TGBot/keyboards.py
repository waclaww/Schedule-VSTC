from telebot import types

kb = types.InlineKeyboardButton

fullSchedule = types.InlineKeyboardMarkup(row_width=1)
fullSchedule.add(
    kb(text="⬅️    На сегодня", callback_data="today", style = "success" ),
    kb(text="➡️      На завтра", callback_data="tomorrow", style = "success"),
    kb(text="      ✍️  Сменить группу", callback_data="change_group", style = "primary")
)

todaySchedule = types.InlineKeyboardMarkup(row_width=1)
todaySchedule.add(
    kb(text="⬅️    На сегодня", callback_data="today", style = "success"),
    kb(text="🔄    Обновить  ", callback_data="update", style = "primary"),
    kb(text="      ✍️  Сменить группу", callback_data="change_group")
)


tomorrowSchedule = types.InlineKeyboardMarkup(row_width=1)
tomorrowSchedule.add(
    kb(text="➡️      На завтра", callback_data="tomorrow", style = "success"),
    kb(text="🔄       Обновить", callback_data="update", style = "primary"),
    kb(text="      ✍️  Сменить группу", callback_data="change_group")
)

def get_schedule_keyboard(current_day):
    kb = types.InlineKeyboardButton
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    if current_day == 'tomorrow':
        markup = todaySchedule
    elif current_day == 'today':  # tomorrow
        markup = tomorrowSchedule
    return markup
