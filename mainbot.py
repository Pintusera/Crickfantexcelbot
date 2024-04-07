import os
import telebot 
from Alive import alive
from datetime import datetime,timedelta
from matchsectc import*

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
    

@bot.message_handler(func=option_func)
def options(message):
    dt_list=option_date()
    markup types. ReplyKeyboardMarkup(row_width=2)
    dtbtn1 types. KeyboardButton(dt_list[0])
    dtbtn2 = types. KeyboardButton(dt_list[1])
    dtbtn3 = types.KeyboardButton(dt_list[2])
    dtbtn4 = types.KeyboardButton(dt_list[3])
    markup.add(dtbtnl, dtbtn2,dtbtn3,dtbtn4)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)
    df=matchselec.dataframe()
    ds_match=df.match
	ds_link=df.link
	df=df[df.match==ds_match[1]]
	suffix=df.iat[0,4]

def handle_excel_request(message):
  user_data = message.text.strip() 
  


bot.polling()
