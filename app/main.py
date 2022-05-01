from telebot import types
from config import TOKEN
import request_weather
import telebot


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def give_weathe(message):
    bot.send_message(message.chat.id, request_weather.template)
  
    if request_weather.data["weather"][0]["description"] == 'overcast clouds':    
        img = open("images/overcast_clouds.png", 'rb')
        bot.send_photo(message.chat.id, img)

    elif request_weather.data["weather"][0]["description"] == 'clear sky':
        img = open("images/clear_sky.png", 'rb')
        bot.send_photo(message.chat.id, img)
    
    elif request_weather.data["weather"][0]["description"] == 'light snow':
        img = open("images/snow.png", 'rb')
        bot.send_photo(message.chat.id, img)
    
    elif request_weather.data["weather"][0]["description"] == 'light rain':
        img = open("images/rain.png", 'rb')
        bot.send_photo(message.chat.id, img)


    bot.send_message(message.chat.id, request_weather.etc)



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Змінити місто':
            bot.send_message(message.chat.id, 'Напиши місто, якого хочеш дізнатися погоду: ')
            bot.register_next_step_handler(message, change_city)
        
        else:
            bot.send_message(message.chat.id, message.text)


# RUN bot name is @weather_for_my_daddy_bot
bot.polling(none_stop=True)
