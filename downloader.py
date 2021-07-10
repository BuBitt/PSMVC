from __future__ import unicode_literals
import youtube_dl
from colorama import *
from menu import *
import cut


def my_hook(d):
    if d['status'] == 'finished':
        print('Baixado, convertendo ...')


def dl_options():
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'outtmpl': 'clips/' + cut.s_name + '/1 raw',
        'progress_hooks': [my_hook],
    }
    return ydl_opts


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
    with youtube_dl.YoutubeDL(dl_options()) as ydl:
        ydl.download([url])


menu_top()
url()
