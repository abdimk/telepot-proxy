from pytube import Youtube
from pytube import playlsit

url = 'https://youtu.be/DXUAyRRkI6k'
ytd = Youtube(url).streams.first().download()
print(ytd)
