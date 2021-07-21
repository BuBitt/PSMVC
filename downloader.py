from __future__ import unicode_literals
from pytube import YouTube
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
    f_url = input(Fore.BLUE + '* Cole o link do vídeo: ').replace(' ', '')


def download_video(url):
    yt = YouTube(url)
    msgs.downloader()
    print('* Iniciando Download.')
    (yt.streams
       .filter(progressive=True, res='720p')
       .desc()
       .first()
       .download(output_path=os.path.join('clips', cut.s_name, 'original'), filename='raw')
    )
    print('* Download Finalizado.')


def dl_download_video(url):
    msgs.downloader()  # Downloader message

    with youtube_dl.YoutubeDL(dl_options()) as ydl:
        ydl.download([url])


menu_top()
url()
