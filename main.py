from telebot import TeleBot

bot = TeleBot('7874779259:AAFnZZxObjHWqfCIbRmB-6Ppkg1F3Gn3nwA')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,'Напиши /cska или /spartak или /zenit или /krasnodar или /loko', parse_mode='Markdown')

@bot.message_handler(commands=['cska'])
def main(message):
    bot.send_message(message.chat.id,'http://www.pfc-cska.com', parse_mode='Markdown')


@bot.message_handler(commands=['spartak'])
def main(message):
    bot.send_message(message.chat.id,'http://spartak.com', parse_mode='Markdown')


@bot.message_handler(commands=['zenit'])
def main(message):
    bot.send_message(message.chat.id,'http://www.fc-zenit.ru', parse_mode='Markdown')


@bot.message_handler(commands=['loko'])
def main(message):
    bot.send_message(message.chat.id,'http://fclm.ru', parse_mode='Markdown')

@bot.message_handler(commands=['krasnodar'])
def main(message):
    bot.send_message(message.chat.id,'http://www.fckrasnodar.ru', parse_mode='Markdown')

bot.infinity_polling()