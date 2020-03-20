# -*- coding: utf-8 -*-

import telebot
from telebot import types
import datetime
from random import choice
from config import token

bot = telebot.TeleBot(token)
yes_no = ["Да", "Нет"]
gang = "Преподаватели\nМельникова Елена Петровна\nКособуцкая Екатерина Владимировна\nЖук Арсений Сергеевич\nКалайдина " \
       "Галина Вениаминовна\nЖуков Сергей Александрович\nРубцов Сергей Евгеньевич\nКлимец Александр Александрович "
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
    "0_0": "Понедельник\n1.\n2. [9:40] Конструирование алгоритмов и структур данных📒 (133)\n3. Введение в теорию "
           "параллельных алгоритмов💡 (102)",
    "0_1": "Вторник\n1. Иностранный язык💡(344)\n2. Функциональное и логическое программирование💡 (A301a)\n3. "
           "Физра🏐\n4. Функциональное и логическое программирование📒 (A305)",
    "0_2": "Среда\n1.\n2.\n3. [11:30] Введение в теорию параллельных алгоритмов📒 (129)\n4. Введение в теорию "
           "параллельных алгоритмов💡 (105)",
    "0_3": "Четверг\n1.\n2. [9:40] Основы теории вероятностей и статистических методов📒 (129)\n3. Основы теории "
           "вероятностей и статистических методов💡 (A301б)\n",
    "0_4": "Пятница\n1.\n2. [9:40] Конструирование алгоритмов и структур данных💡 (102)\n3. Физра🏐\n4. Физические "
           "основы микроэлектроники📒 (A307)",
    "0_5": "Суббота\n1. Теория алгоритмов и вычислительных процессов💡 (106a)\n2. Конструирование алгоритмов и "
           "структур данных💡 (A301a)\n3. Теория алгоритмов и вычислительных процессов📒 (129) ",
    "1_7": "Понедельник\n1.\n2. [9:40] Конструирование алгоритмов и структур данных📒 (133)\n3. Введение в теорию "  # понедельник числителя 
           "параллельных алгоритмов💡 (102)"  # понедельник знаменателя
}
activity_denominator = {
    "1_0": "1. Иностранный язык💡(100С)\n2. Конструирование алгоритмов и структур данных📒 (133)",
    "1_1": "Вторник\n1. Иностранный язык💡(344)\n2. Функциональное и логическое программирование💡 (A301a)\n3. "
           "Физра🏐\n4. Функциональное и логическое программирование📒 (A305)",
    "1_2": "Среда\n1.\n2.\n3. [11:30] Введение в теорию параллельных алгоритмов📒 (129)\n4. Введение в теорию "
           "параллельных алгоритмов💡 (105)",
    "1_3": "Четверг\n1.\n2. [9:40] Основы теории вероятностей и статистических методов📒 (129)\n3. Основы теории "
           "вероятностей и статистических методов💡 (A301б)\n4. Теория алгоритмов и вычислительных процессов💡 (101)",
    "1_4": "Пятница\n1. Физические основы микроэлектроники💡 (133)\n2. Конструирование алгоритмов и структур данных💡 "
           "(102)\n3. Физра🏐\n4. Физические основы микроэлектроники📒 (A307)",
    "1_5": "Суббота\n1. Теория алгоритмов и вычислительных процессов💡 (106a)\n2. Конструирование алгоритмов и "
           "структур данных💡 (A301a)\n3. Теория алгоритмов и вычислительных процессов📒 (129) ",
    "1_7": "Понедельник\n1.\n2. [9:40] Конструирование алгоритмов и структур данных📒 (133)\n3. Введение в теорию "
           "параллельных алгоритмов💡 (102)"  # понедельник числителя
}


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Выбирай, {message.chat.first_name}", reply_markup=start_keyboard())


def start_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text="Числитель", callback_data="numerator")
    button2 = types.InlineKeyboardButton(text="Знаменатель", callback_data="denominator")
    button4 = types.InlineKeyboardButton(text="ФИО преподов", callback_data="fio")
    button5 = types.InlineKeyboardButton(text="Съебать с пары?", callback_data="question")
    button6 = types.InlineKeyboardButton(text="Числитель или знаменатель?", callback_data="num_denom")
    button7 = types.InlineKeyboardButton(text="На сегодня", callback_data="today")
    button8 = types.InlineKeyboardButton(text="На завтра", callback_data="tomorrow")
    keyboard.add(button1, button2)
    keyboard.add(button6)
    keyboard.add(button7, button8)
    keyboard.add(button4)
    keyboard.add(button5)
    return keyboard


def days_keyboard_0():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    button0 = types.InlineKeyboardButton(text="Понедельник", callback_data="0_0")
    button1 = types.InlineKeyboardButton(text="Вторник", callback_data="0_1")
    button2 = types.InlineKeyboardButton(text="Среда", callback_data="0_2")
    button3 = types.InlineKeyboardButton(text="Четверг", callback_data="0_3")
    button4 = types.InlineKeyboardButton(text="Пятница", callback_data="0_4")
    button5 = types.InlineKeyboardButton(text="Суббота", callback_data="0_5")
    button6 = types.InlineKeyboardButton(text="Назад", callback_data="main_menu")
    keyboard.add(button0, button1, button2)
    keyboard.add(button3, button4, button5)
    keyboard.add(button6)
    return keyboard


def days_keyboard_1():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    button0 = types.InlineKeyboardButton(text="Понедельник", callback_data="1_0")
    button1 = types.InlineKeyboardButton(text="Вторник", callback_data="1_1")
    button2 = types.InlineKeyboardButton(text="Среда", callback_data="1_2")
    button3 = types.InlineKeyboardButton(text="Четверг", callback_data="1_3")
    button4 = types.InlineKeyboardButton(text="Пятница", callback_data="1_4")
    button5 = types.InlineKeyboardButton(text="Суббота", callback_data="1_5")
    button6 = types.InlineKeyboardButton(text="Назад", callback_data="main_menu")
    keyboard.add(button0, button1, button2)
    keyboard.add(button3, button4, button5)
    keyboard.add(button6)
    return keyboard


def result_keyboard_0():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button0 = types.InlineKeyboardButton(text="Назад", callback_data="back0")
    button1 = types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    keyboard.add(button0, button1)
    return keyboard


def result_keyboard_1():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button0 = types.InlineKeyboardButton(text="Назад", callback_data="back1")
    button1 = types.InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    keyboard.add(button0, button1)
    return keyboard


def today_tomorrow_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text="Назад", callback_data="main_menu")
    keyboard.add(button1)
    return keyboard


def fio_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text="Назад", callback_data="main_menu")
    keyboard.add(button1)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "main_menu":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"Выбирай, {call.message.chat.first_name}", reply_markup=start_keyboard())
    if call.data == "back0":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="На какой день по числителю?",
                              reply_markup=days_keyboard_0())
    if call.data == "back1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="На какой день по знаменателю?",
                              reply_markup=days_keyboard_1())
    if call.data == "numerator":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="На какой день по числителю?",
                              reply_markup=days_keyboard_0())
    if call.data == "0_0" or call.data == "0_1" or call.data == "0_2" or call.data == "0_3" or call.data == "0_4" or call.data == "0_5":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=activity_numerator.get(call.data),
                              reply_markup=result_keyboard_0())
    if call.data == "denominator":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="На какой день по знаменателю?",
                              reply_markup=days_keyboard_1())
    if call.data == "1_0" or call.data == "1_1" or call.data == "1_2" or call.data == "1_3" or call.data == "1_4" or call.data == "1_5":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=activity_denominator.get(call.data),
                              reply_markup=result_keyboard_1())
    if call.data == "today":
        if datetime.datetime.today().weekday() == 6:
            bot.answer_callback_query(call.id, "Долбаеб, сегодня воскресенье")
        else:
            if datetime.datetime.now().isocalendar()[1] % 2 == 0:
                numerator_key = "0_" + str(datetime.datetime.today().weekday())
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=activity_numerator.get(numerator_key),
                                      reply_markup=today_tomorrow_keyboard())
            else:
                denominator_key = "1_" + str(datetime.datetime.today().weekday())
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=activity_denominator.get(denominator_key),
                                      reply_markup=today_tomorrow_keyboard())
    if call.data == "tomorrow":
        if datetime.datetime.today().weekday() + 1 == 6:
            bot.answer_callback_query(call.id, "Долбаеб, завтра воскресенье")

        else:
            if datetime.datetime.now().isocalendar()[1] % 2 == 0:
                numerator_key = "0_" + str(datetime.datetime.today().weekday() + 1)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=activity_numerator.get(numerator_key),
                                      reply_markup=today_tomorrow_keyboard())
            else:
                denominator_key = "1_" + str(datetime.datetime.today().weekday() + 1)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=activity_denominator.get(denominator_key),
                                      reply_markup=today_tomorrow_keyboard())
    if call.data == "fio":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=gang, reply_markup=fio_keyboard())
    if call.data == "question":
        bot.answer_callback_query(call.id, choice(yes_no))
    if call.data == "num_denom":
        if datetime.datetime.now().isocalendar()[1] % 2 == 0:
            bot.answer_callback_query(call.id, days.get((datetime.datetime.today().weekday())) + ", числитель.")
        else:
            bot.answer_callback_query(call.id, days.get((datetime.datetime.today().weekday())) + ", знаменатель.")


if __name__ == '__main__':
    bot.polling(none_stop=True)



