
from telegram.ext import Updater,CommandHandler
import requests  # Getting the data from the cloud
import os
from Adafruit_IO import Client, Feed , Data


aio = Client(os.getenv('ADAFRUIT_IO_USERNAME'),os.getenv('ADAFRUIT_IO_KEY'))


def last(bot,update):
    data = aio.data('bot')
    count=0
    values=""
    for d in data:
        count+=1
        if d.value=="1":values+="ON\n"
        elif d.value=="0":values+="OFF\n"
        if count==10:break
        
    chat_id = update.message.chat_id
    bot.send_message(chat_id,values)
    
def light_on(bot,update):
    value= Data(value=1)
    value_send=aio.create_data('bot',value)
    chat_id = update.message.chat_id
    bot.send_message(chat_id,'The light is now ON.')
    bot.send_photo(chat_id, photo=open('light_on.jpg', 'rb'))

def light(bot,update):
    data = aio.receive('bot')
    if data.value=="1":
        chat_id = update.message.chat_id
        bot.send_message(chat_id,'The light is currently ON.')
        bot.send_photo(chat_id, photo=open('light_on.jpg', 'rb'))
    elif data.value=="0":
        chat_id = update.message.chat_id
        bot.send_message(chat_id,'The light is currently OFF.')
        bot.send_photo(chat_id, photo=open('light_off.jpg', 'rb'))


def light_off(bot,update):
    value= Data(value=0)
    value_send=aio.create_data('bot',value)
    chat_id = update.message.chat_id
    bot.send_message(chat_id,'The light is now OFF.')
    bot.send_photo(chat_id, photo=open('light_off.jpg', 'rb'))

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def dog(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id,photo=url)


u = Updater('1368495354:AAEs2hs_nVNjhgwog36BOMIS3jX4raZ3bLQ')
dp = u.dispatcher
dp.add_handler(CommandHandler('dog',dog))
dp.add_handler(CommandHandler('light',light))
dp.add_handler(CommandHandler('light_on',light_on))
dp.add_handler(CommandHandler('light_off',light_off))
dp.add_handler(CommandHandler('prev_values',last))
u.start_polling()
u.idle()
