import telebot
from telebot import types
import time
from datetime import datetime
import openai


bot = telebot.TeleBot('6687074088:AAGOXXpE-KaUiE7iTBfnxqXMVdGGwvQquVk');
openai.api_key = "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"
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет! /button")
@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("get_my_ip")
    item2 = types.KeyboardButton("yandex_music")
    item3 = types.KeyboardButton("time_to_omsk")
    # item4 = types.KeyboardButton("chat_gpt")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    # markup.add(item4)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет" or message.text.lower() == "сколько":
        bot.send_message(message.from_user.id, "Сейчас напишу оставшееся время")
        n_now = datetime.strptime(datetime.now().strftime("%d.%m.%Y %H:%M:%S"), "%d.%m.%Y %H:%M:%S")
        tm_dlt = datetime(2023, 12, 30, 21, 45) - n_now
        days, hours, minutes, seconds = (tm_dlt.days,
                                         tm_dlt.seconds // 3600,
                                         (tm_dlt.seconds - tm_dlt.seconds // 3600 * 3600) // 60,
                                         tm_dlt.seconds - tm_dlt.seconds // 3600 * 3600 - (
                                                 tm_dlt.seconds - tm_dlt.seconds // 3600 * 3600) // 60 * 60)
        bot.send_message(message.from_user.id, f"Осталось: ~ {days} дней  {hours}ч. {minutes}м. {seconds}с.")
        def repeated_action():
            total_sec = 1
            while total_sec > 0:
                n_now = datetime.strptime(datetime.now().strftime("%d.%m.%Y %H:%M:%S"), "%d.%m.%Y %H:%M:%S")
                tm_dlt = datetime(2023, 12, 30, 21, 45) - n_now
                total_sec = int(tm_dlt.total_seconds())
                days, hours, minutes, seconds = (tm_dlt.days,
                                                 tm_dlt.seconds // 3600,
                                                 (tm_dlt.seconds - tm_dlt.seconds // 3600 * 3600) // 60,
                                                 tm_dlt.seconds - tm_dlt.seconds // 3600 * 3600 - (
                                                         tm_dlt.seconds - tm_dlt.seconds // 3600 * 3600) // 60 * 60)
                bot.send_message(message.from_user.id, f"Осталось: ~ {days} дней  {hours}ч. {minutes}м. {seconds}с.")
                time.sleep(60)
    elif message.text == "get_my_ip":
        bot.send_message(message.chat.id,"https://2ip.ru/")
    elif message.text == "yandex_music":
        bot.send_message(message.chat.id,"https://music.yandex.ru/home")
    elif message.text == "time_to_omsk":
        bot.send_message(message.from_user.id, "Сейчас напишу оставшееся время")
        n_now = datetime.strptime(datetime.now().strftime("%d.%m.%Y %H:%M:%S"), "%d.%m.%Y %H:%M:%S")
        tm_dlt = datetime(2023, 12, 30, 21, 45) - n_now
        days, hours, minutes, seconds = (tm_dlt.days,
                                         tm_dlt.seconds // 3600,
                                         (tm_dlt.seconds - tm_dlt.seconds // 3600 * 3600) // 60,
                                         tm_dlt.seconds - tm_dlt.seconds // 3600 * 3600 - (
                                                 tm_dlt.seconds - tm_dlt.seconds // 3600 * 3600) // 60 * 60)
        bot.send_message(message.from_user.id, f"Осталось: ~ {days} дней  {hours}ч. {minutes}м. {seconds}с.")
    # elif message.text == "chat_gpt":
    #     bot.send_message(message.from_user.id, "введи запрос")
    #     @bot.message_handler(content_types=['text'])
    #     def get_answer(new_message):
    #         bot.send_message(message.from_user.id, "я здесь")
    #         # if new_message.text:
    #         messages_data = []
    #         messages_data.append({"role": "user", "content": new_message.text})
    #         chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_data)
    #         reply = chat.choices[0].message.content
    #         bot.send_message(message.from_user.id, f"ChatGPT: {reply}")
    #         messages_data.append({"role": "assistant", "content": reply})a
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет или сколько")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)