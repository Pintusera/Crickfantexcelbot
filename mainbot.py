

import telebot

BOT_TOKEN = token

bot = telebot.TeleBot(BOT_TOKEN)

def handle_excel_request(message):
  user_data = message.text.strip()  # Get user input (data for Excel)



bot.polling()
