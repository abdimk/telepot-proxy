import telepot
from telepot.loop import MessageLoop


token = '1351679001:AAG3Tvel8T2y2NTY2jPrKRZUhz-WZmLfD9U'


def setfiy(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type ==['text']:
        if msg['text'] =='/start':
            bot.sendMessage(
                chat_id,f'hello world',reply_markup=None
            )
bot = telepot.Bot(token)
MessageLoop(bot, {'chat':setfiy}).run_as_thread()
