import requests
import telebot
from datetime import datetime
from testtoken import token1
from weathertoken import token2


url = 'http://api.openweathermap.org/data/2.5/weather'
weather_token = token2
bot = telebot.TeleBot(token1)


@bot.message_handler(commands=['start'])
def welcome (message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBg6dfmw4FeA5qmVYRDi1IAUlGcXsHRgACewsAAi8P8AayZLS40eVepRsE')
    bot.send_message(message.chat.id, 'Hi, {0.first_name}!\nI am - <b>{1.first_name}</b> bot'.format(message.from_user, bot.get_me()), parse_mode='html')

@bot.message_handler(commands=['help'])
def welcome (message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBg75fmyjKyBW8Z88dnBYjWT9fZRAj7QACgQsAAi8P8AbXgANmmwlPZxsE')
    bot.send_message(message.chat.id, "I'm just learning, so for starters, I can show you the weather in any city you want.\nYou just need to write  <b>name of city</b> and that's it. \nFor correct work, try to write the name of the city in English.", parse_mode='html')

@bot.message_handler(content_types=["text"])
def weather (message):
    s_city = message.text
    try:
        params = {'appid': weather_token, 'q': s_city, 'units': 'metric', 'lang': 'ua'}
        result = requests.get(url, params=params)
        weather = result.json()
        bot.send_message(message.chat.id, "Зараз у місті - "  + str(weather["name" ])  + " " + str(float(weather["main"]['temp'])) + " °C" +"\n" +
                         "Максимальна температура: " + str(float(weather['main']['temp_max'])) + " °C" + "\n" +
                         "Мінімальна  температура: " + str(float(weather['main']['temp_min'])) + " °C" +"\n" +
                         "Швидкість вітру: " + str(float(weather['wind']['speed'])) + "\n" +
                         "Вологість: " + str(float(weather['main']['humidity'])) + "\n" 
                         "На вулиці: " + str(weather['weather'][0]["description"]) + "\n")

        if weather["main"]['temp'] < 10:
            bot.send_message(message.chat.id, "Зараз холодно!")
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBg7BfmyHJlrhWCaW6gXiMBmSSCKQaFwACLgADO2AkFBcnim9TCd1FGwQ')

        elif weather["main"]['temp'] < 20:
            bot.send_message(message.chat.id, "Зараз прохолодно!")
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBg7ZfmySeG_3DNnX4dTvchhuQdyo-1gACfQsAAi8P8AbfOHuM4D0mfRsE')

        elif weather["main"]['temp'] > 30:
            bot.send_message(message.chat.id, "Зараз жарко!")
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBg7JfmyQ4DyTqgi1YDtC0XfXjyiq9uQACDwADwDZPEwXo1IXy1A6fGwQ')

        else:
            bot.send_message(message.chat.id, "Зараз чудова температура!")
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBg7RfmySTW7Zby9Ak5Hb7PFZ8gaU-2QACeAsAAi8P8AaM37uPS0xUihsE')

    except:
        bot.send_message(message.chat.id, "Місто " + s_city + " не знайдено")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBg7hfmyUcDIai2hAghHSOQB08GcGuAQAC5QADVp29CggLFmSVBdGKGwQ')

@bot.message_handler(content_types=['sticker'])
def text_handler(message):
    bot.send_message(message.chat.id, "Sorry, I can't analyze stickers yet")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBg8BfmyoWXB8lL2MPrbf8wuVqy9017gACWAQAAonq5QfkU4puMGYL8hsE')

@bot.message_handler(content_types=['photo'])
def text_handler(message):
    bot.send_message(message.chat.id, "Sorry, I can't analyze yet, but I'm sure this photo is beautiful")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBg8JfmytOstJAHNLKsmfBeZT7VFOGHwACEQADWbv8JctzvPnr-GDyGwQ')

bot.polling()
