import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


class MyClass():
    def __init__(self):
        self.file_capt = 'Caption'

    def store_it(self, fileID):
        self.file_capt = fileID

    def retrieve(self, capt_ion, chat_id):
        try:
            bot.sendDocument('@tricksgum', self.file_capt, caption=capt_ion)
            bot.sendMessage(chat_id, 'Successfully sent')

        except:
            bot.sendMessage(
                chat_id, 'Please try again with a shorter caption!')


file_share = MyClass()
token = '773013352:AAEob_--s_0m9BThpmH9RxVO8yQ7KoaLiYc'
keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Send File')]], resize_keyboard=True)


def fileShareFunction(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'document':
        fileID = (msg['document']['file_id'])
        bot.sendMessage(
            chat_id, 'Now send the file caption less than 1024 characters with # eg #Darkest Minds')
        file_share.store_it(fileID)

    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(
                chat_id, 'Hi, i can help you send any file to your channel', reply_markup=keyboard)

        if msg['text'] == 'Send File':
            bot.sendMessage(
                chat_id, 'Forward to me any file from any other channel')

        if '#' in msg['text']:
            capt_ion = msg['text'][1:] + "\n \n @tricksgum"
            file_share.retrieve(capt_ion, chat_id)


bot = telepot.Bot(token)
MessageLoop(bot, {'chat': fileShareFunction}).run_as_thread()
