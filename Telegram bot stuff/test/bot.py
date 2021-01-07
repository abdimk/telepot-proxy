import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
# start of online server proxy config

import urllib3
import telepot.api
proxy_url = 'http://proxy.server:3128'

telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30), }

telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1,
                                                             retries=False, timeout=30))

# end of online server proxy config


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='abdisa😊', callback_data='hello word')],
    ])

    bot.sendMessage(
        chat_id, 'Hello there this is connie the most advanced telegram chat bot', reply_markup=keyboard)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(
        msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')


TOKEN = "1180712921:AAEn9ENyX2faW4I-OT7nuEzDhpz6zESWDT0"

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Server running ...')

while 1:
    time.sleep(10)
