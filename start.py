from upgrade import *
from prereq import *
from downloader import *
from cut import *
import msgs


def start():
    session_name()                  # Cria o nome de seção
    msgs.select_cuts()              # Cabeçalho da seleção de cortes
    times_input()                   # Define os tempos de corte
    download_video(f_url)           # Baixa vídeo
    clip_cut(times)                 # Corta vídeo
    msgs.final()                    # Mensagem de CONCLUÍDO


start()
