from time import strftime, gmtime, sleep
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent


token = '1322966057:AAHX1WBp2n6faKr_912UNbeUqs_61rpvRbw'


def fileShareFunction(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'] == '/start':
            marku1 = InlineKeyboardMarkup(
                inline_keyboard=[[dict(text='Telegram URL', url='https://core.telegram.org/'), dict(text='google URL', url='https://core.telegram.org/')], [dict(text='onion blast😎', url='https://t.me/carvor')]])
            bot.sendMessage(
                chat_id, 'Hello there send me google url then am gonna send you the photo', reply_markup=marku1)
            photo_url2 = 'https://images.app.goo.gl/3KUGV3hd6FHvTgPA7'
            bot.sendPhoto(chat_id,photo=photo_url2,reply_markup=None)
            video_url = 'https://youtu.be/DXUAyRRkI6k'
            bot.sendVideo(
                chat_id, video = video_url,reply_markup=None
            )
            
    if content_type =='text':
        if msg['text']:
            photo_url = msg['text']
            bot.sendPhoto(
                chat_id,photo = photo_url,reply_markup=None
            )


bot = telepot.Bot(token)
MessageLoop(bot, {'chat': fileShareFunction}).run_as_thread()
