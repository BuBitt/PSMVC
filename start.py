from downloader import *
from settings import *
from prereq import *
from cut import *
import fileinput
import sys


if p_req_inst:
    pre_req()
    for i, line in enumerate(fileinput.input('settings.py', inplace=1)):
        sys.stdout.write(line.replace('True', 'False'))


def start():
    session_name()                  # Cria o nome de seção
    times_input()                   # Define os tempos de corte
    download_video(f_url)           # Baixa vídeo
    clip_cut(times)                 # Corta vídeo
    final()                         # Mensagem de CONCLUÍDO


start()
