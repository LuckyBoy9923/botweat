import pyowm
import telebot

owm = pyowm.OWM('1672f972ebc3d4a485ead6db03472d37')
bot = telebot.TeleBot("678615806:AAEEwOXyjBMvwhgnuPrVb1dsT-1rRbL0l6Y")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = " В городе "  + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура сейчас в районе " + str(temp) + "\n\n"

	if temp < 10:
		answer += "Сейчас ппц как холодно одевайся как танк!"
	elif temp < 20:
		answer += "Сегодня холодно, оденься потеплее."
	else:
		answer += "Температура нормальная,одевай что угодно."
	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )