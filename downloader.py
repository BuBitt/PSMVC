from __future__ import unicode_literals
import youtube_dl
from colorama import *
from menu import *


def my_hook(d):
    if d['status'] == 'finished':
        print('Baixado, convertendo ...')


ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'outtmpl': 'temp/1',
    'progress_hooks': [my_hook],
}


def url():
    global f_url
    f_url = input(Fore.BLUE + '* Cole o link do vídeo: ')

def download_video(url):
    print(Fore.BLUE + """
----------------------------------------------------------

           ================================
            INICIANDO PROCESSO DE DOWNLOAD
           ================================

------------------------------------------------------------""")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


menu_top()
url()
