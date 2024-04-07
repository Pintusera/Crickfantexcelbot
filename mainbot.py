import os
import telebot 
from Alive import alive
from datetime import datetime,timedelta


alive()

BOT_TOKEN =os.environ.get('token')

bot = telebot.TeleBot(BOT_TOKEN)

def option_date():
    date_list=[]
    n=0
    while (n==3):
        date = datetime.now()+timedelta(days=n)
        n+=1
        date_list.append(date.strftime('%a, %d %B'))
    return date_list


@bot.message_handler(commands=['start' , 'Start'])
def start(message):
    bot.reply_to(message, "Hi! I can provide Excel files of any Criket match from ESPNcricinfo website\n"
                          "Enter the corresponding match link.")
@bot.message_handler(func=lambda message: True)
def handle_link(message):
    provide_link = message.text
    print(provide_link)
    bot.send_message(message.chat.id, "wait we are preparing Excel file")
    final(provide_link)
    bot.send_document(message.chat.id, name, caption='Here is your Excel file!')
    bot.send_message(message.chat.id, "done")


def handle_excel_request(message):
  user_data = message.text.strip() 
  


bot.polling()
