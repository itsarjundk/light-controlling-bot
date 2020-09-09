
from telegram.ext import Updater,CommandHandler
import requests  # Getting the data from the cloud

from Adafruit_IO import Client, Feed , Data
x = "arjundk" #ADAFRUIT_IO_USERNAME
y = "aio_UNkx56cfSTlfzXVGKFZ9JdXxxD0S" #ADAFRUIT_IO_KEY

aio = Client(x,y)

def light_on(bot,update):
    value= Data(value=1)
    value_send=aio.create_data('bot',value)
    chat_id = update.message.chat_id
    bot.send_message(chat_id,'The light is ON.')
    bot.send_photo(chat_id, photo=open('light_on.jpg', 'rb'))

def light_off(bot,update):
    value= Data(value=0)
    value_send=aio.create_data('bot',value)
    chat_id = update.message.chat_id
    bot.send_message(chat_id,'The light is OFF.')
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
dp.add_handler(CommandHandler('light_on',light_on))
dp.add_handler(CommandHandler('light_off',light_off))
u.start_polling()
u.idle()
