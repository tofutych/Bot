import telebot
from telebot import types
import datetime
from random import choice

bot = telebot.TeleBot("1315033058:AAG6690TbiPaH5f20LJrwnUMHe4r1QCC2P0")
days = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье"
}
activity_numerator = {
    "0_0": "Понедельник\n1.\n2. [9:40] Интерпретируемые ЯП 📒\n3. Основы компьютерной графики💡",
    "0_1": "Вторник\n1. [8:00] Основы психологии 💡\n2. Основы психологии 📒",
    "0_2": "Среда\n1.\n2. [9:40] Управление информацией 📍📒\n3. Физра 🏐\n4. Компьютерные сети 💡\n5. Основы комп. лингвистики 📒",
    "0_3": "Четверг\n1.\n2.\n3. [11:30] Компьютерные сети 💡\n4. Операционные системы 💡\n5. Компьютерные сети 📒",
    "0_4": "Пятница\n1.\n2.\n3.\n4. [13:10] Информационная безопасность 📒\n5. Управление информацией 💡\n6. Компьютерные сети 📒\n7. Информационная безопасность 💡",
    "0_7": "Понедельник\n1.\n2. [9:40] Интерпретируемые ЯП 💡\n3. Интерпретируемые ЯП 💡\n4. Операционные системы 💡"  # понедельник знаменателя

}
activity_denominator = {
    "1_0": "Понедельник\n1.\n2. [9:40] Интерпретируемые ЯП 💡\n3. Интерпретируемые ЯП 💡\n4. Операционные системы 💡",
    "1_1": "Вторник\n1. [8:00] Основы психологии 💡\n2. Основы компьютерной графики 📒",
    "1_2": "Среда\n1. [8:00] Интерпретируемые ЯП 💡\n2. Управление информацией 📍📒\n3. Физра 🏐\n4. Основы компьютерной лингвистики 📍📒",
    "1_3": "Четверг\n1.\n2.\n3. [11:30] Операционные системы 💡\n4. Операционные системы 💡\n5. Компьютерные сети 📒",
    "1_4": "Пятница\n1.\n2. [9:40] Управление информацией 💡\n3. Компьютерные сети 💡\n4. Информационная безопасность 📒\n5. Информационная безопасность 💡\n6. Иностранный язык 💡",
    "1_7": "Понедельник\n1.\n2. [9:40] Интерпретируемые ЯП 📒\n3. Основы компьютерной графики💡"  # понедельник числителя
}
eblan = ["Я", "Ты"]


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Выбирай, {message.chat.first_name}!", reply_markup=start_keyboard())


def start_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    button1 = types.InlineKeyboardButton(text="Числитель",
                                         callback_data="numerator")

    button2 = types.InlineKeyboardButton(text="Знаменатель",
                                         callback_data="denominator")

    button3 = types.InlineKeyboardButton(text="На сегодня",
                                         callback_data="today")

    button4 = types.InlineKeyboardButton(text="На завтра",
                                         callback_data="tomorrow")
    button5 = types.InlineKeyboardButton(text="Кто еблан?",
                                         callback_data="eblan")

    keyboard.add(button1, button2)
    keyboard.add(button3)
    keyboard.add(button4)
    keyboard.add(button5)
    return keyboard


def days_keyboard_0():
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    button0 = types.InlineKeyboardButton(text="Понедельник",
                                         callback_data="0_0")

    button1 = types.InlineKeyboardButton(text="Вторник",
                                         callback_data="0_1")

    button2 = types.InlineKeyboardButton(text="Среда",
                                         callback_data="0_2")

    button3 = types.InlineKeyboardButton(text="Четверг",
                                         callback_data="0_3")

    button4 = types.InlineKeyboardButton(text="Пятница",
                                         callback_data="0_4")

    button5 = types.InlineKeyboardButton(text="Назад ↩",
                                         callback_data="main_menu")

    keyboard.add(button0, button1)
    keyboard.add(button2, button3)
    keyboard.add(button4, button5)
    return keyboard


def result_keyboard_0():
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    button0 = types.InlineKeyboardButton(text="Назад", callback_data="back0")

    button1 = types.InlineKeyboardButton(text="Главное меню",
                                         callback_data="main_menu")

    keyboard.add(button0, button1)
    return keyboard


def days_keyboard_1():
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    button0 = types.InlineKeyboardButton(text="Понедельник",
                                         callback_data="1_0")

    button1 = types.InlineKeyboardButton(text="Вторник",
                                         callback_data="1_1")

    button2 = types.InlineKeyboardButton(text="Среда",
                                         callback_data="1_2")

    button3 = types.InlineKeyboardButton(text="Четверг",
                                         callback_data="1_3")

    button4 = types.InlineKeyboardButton(text="Пятница",
                                         callback_data="1_4")

    button5 = types.InlineKeyboardButton(text="Назад ↩",
                                         callback_data="main_menu")

    keyboard.add(button0, button1)
    keyboard.add(button2, button3)
    keyboard.add(button4, button5)
    return keyboard


def result_keyboard_1():
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    button0 = types.InlineKeyboardButton(text="Назад", callback_data="back1")

    button1 = types.InlineKeyboardButton(text="Главное меню",
                                         callback_data="main_menu")

    keyboard.add(button0, button1)
    return keyboard


def today_tomorrow_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text="Назад", callback_data="main_menu")
    keyboard.add(button1)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "main_menu":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=f"Выбирай, {call.message.chat.first_name}!",
                              reply_markup=start_keyboard())

    if call.data == "back0":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="На какой день по числителю?",
                              reply_markup=days_keyboard_0())

    if call.data == "back1":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="На какой день по знаменателю?",
                              reply_markup=days_keyboard_1())

    if call.data == "numerator":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="На какой день по числителю?",
                              reply_markup=days_keyboard_0())

    if call.data == "denominator":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="На какой день по знаменателю?",
                              reply_markup=days_keyboard_1())

    if call.data[0] == "0":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=activity_numerator.get(call.data),
                              reply_markup=result_keyboard_0())

    if call.data[0] == "1":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=activity_denominator.get(call.data),
                              reply_markup=result_keyboard_1())

    if call.data == "today":
        if datetime.datetime.today().weekday() == (5 or 6):
            bot.answer_callback_query(call.id, "Долбаеб, сегодня выходной")
        else:
            if datetime.datetime.now().isocalendar()[1] % 2 == 0:
                numerator_key = "0_" + str(datetime.datetime.today().weekday())
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=activity_numerator.get(numerator_key),
                                      reply_markup=today_tomorrow_keyboard())
            else:
                denominator_key = "1_" + str(datetime.datetime.today().weekday())
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=activity_denominator.get(denominator_key),
                                      reply_markup=today_tomorrow_keyboard())

    if call.data == "tomorrow":
        if datetime.datetime.today().weekday() + 1 == (5 or 6):
            bot.answer_callback_query(call.id, "Долбаеб, завтра выходной")
        else:
            if datetime.datetime.now().isocalendar()[1] % 2 == 0:
                numerator_key = "0_" + str(datetime.datetime.today().weekday() + 1)
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=activity_numerator.get(numerator_key),
                                      reply_markup=today_tomorrow_keyboard())
            else:
                denominator_key = "1_" + str(datetime.datetime.today().weekday() + 1)
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text=activity_denominator.get(denominator_key),
                                      reply_markup=today_tomorrow_keyboard())

    if call.data == "eblan":
        bot.answer_callback_query(call.id, choice(eblan))
        photo = open('/tmp/photo.png', 'rb')


if __name__ == '__main__':
    bot.polling(none_stop=True)
