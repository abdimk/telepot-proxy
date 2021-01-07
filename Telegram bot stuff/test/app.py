from time import strftime, gmtime
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


token = '1005995344:AAGTdxcVKNkf4878p9xE7eCJD04z-xIulc4'


def fileShareFunction(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    time_now = strftime('%c', gmtime())
    time_now_day = strftime('%A', gmtime())
    time_now_month = strftime('%B', gmtime())
    time_year = strftime('%C', gmtime())
    time_local = strftime('%X', gmtime())
    day_month_year = strftime('%D', gmtime())
    time_hour = strftime('%H', gmtime())
    time_min = strftime('%M', gmtime())
    time_sec = strftime('%S', gmtime())
    time_weekday = strftime('%w', gmtime())
    time_zone_number = strftime('%U', gmtime())
    time_zone = strftime('%Z', gmtime())


    if content_type == 'text':
        value = f"""
The time is {time_now}
\n
functions about time on python3.8 time module
time_now_day = {time_now_day} 
time_now_month = {time_now_month}
time_year = {time_year}
time_local = {time_local}
day_month_year = {day_month_year}
time_hour = {time_hour}
time_min = {time_min}
time_sec = {time_sec}
time_weekday = {time_weekday}
time_zone_number = {time_zone_number}
time_zone = {time_zone}
"""
        if msg['text'] == '/start':
            bot.sendMessage(
                chat_id, f' Hey there ! the time is {time_now}\n for more info /gettime', reply_markup=None)
        if msg['text'] == '/gettime':
            bot.sendMessage (
                chat_id, f'{value}', reply_markup=None)
            bot.sendPhoto(chat_id,)
        if time_hour == '6':
            bot.sendMessage(
                chat_id,f'Good morning 😇 the time is {time_hour}', reply_markup=None)



bot = telepot.Bot(token)
MessageLoop(bot, {'chat': fileShareFunction}).run_as_thread()
