
import os
import telebot
from telegramcrickexcel import final 
from Alive import alive

alive()

BOT_TOKEN =os.environ.get('token')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start' , 'Start'])
def start(message):
    bot.reply_to(message, "Hi! I can provide Excel files of any Criket match from ESPNcricinfo website\n"
                          "Enter the corresponding match link.")
@bot.message_handler(func=lambda message: True)
def handle_link(message):
    provide_link = message.text
    bot.send_message(message.chat.id, "wait we are preparing Excel file")
    name=final(provide_link)
    with open(name, 'rb') as file:
        bot.send_document(message.chat.id, file, caption='Here is your Excel file!')
    bot.send_message(message.chat.id, "done")
    
def handle_excel_request(message):
  user_data = message.text.strip() 
  


bot.polling()
