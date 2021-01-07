import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton




token = '773013352:AAEob_--s_0m9BThpmH9RxVO8yQ7KoaLiYc'


content_type, chat_type, chat_id = telepot.glance(msg)
if content_type == 'text':
    if msg['text'] == '/start':
        bot.sendMessage(chat_id, 'Hi, i can help you send any file to your channel', reply_markup=keyboard)


bot = telepot.Bot(token)
MessageLoop(bot, {'chat'}).run_as_thread()
