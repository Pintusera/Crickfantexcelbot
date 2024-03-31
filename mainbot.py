

import telebot
import telegramcrickexcel
import suprocces
BOT_TOKEN = token

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi! I can provide Excel files of any Criket match from ESPNcricinfo website\n"
                          "Enter the corresponding match link.")
@bot.message_handler(func=lambda message: True)
def handle_link(message):
    link = message.text
    

def handle_excel_request(message):
  user_data = message.text.strip() 
  


bot.polling()
