from __future__ import unicode_literals
import youtube_dl
from menu import *
import cut
import msgs
import os


def my_hook(d):
    if d['status'] == 'finished':
        print('Baixado, convertendo ...')


def dl_options():
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'outtmpl': os.path.join('clips', cut.s_name, 'original', 'raw'),
        'progress_hooks': [my_hook],
    }
    return ydl_opts


def url():

        global f_url
        f_url = input(Fore.BLUE + '* Cole o link do vídeo: ')


def download_video(url):

    msgs.downloader()  # Downloader message

    with youtube_dl.YoutubeDL(dl_options()) as ydl:
        ydl.download([f_url])


menu_top()
url()
