from moviepy.editor import *
from colorama import Fore
from os import *


times = []


def session_name():
    global session_name
    session_name = input('* Dê um nome à sessão: ')
    print("----------------------------------------------------------")


def session(session_name):
    return os.mkdir("clips/" + session_name)


def error_tratament(type_variable, list, stage):
    """Trata os erros de digitação dos tempos"""

    if not type_variable.isdigit():
        while 1:
            print('\n' + Fore.RED + f'  !!!! O valor {stage} digitado não é válido !!!!')
            type_variable = input(f"* Digite o tempo de {stage} do corte novamente (segundos): ")

            if type_variable.isdigit():
                list.append(int(type_variable))
                break
    else:
        list.append(type_variable)


def times_input():
    """Coleta e salva os tempos para os cortes"""

    clip_number = 0

    while 1:
        clip_number += 1
        print('\n' + Fore.GREEN + f'        ========== Corte Nº {clip_number} =========')
        time_init = input("* Início do corte (segundos): ")

        if time_init == '':
            break

        # "Início" ERROR TRATEMENT
        error_tratament(time_init, times, 'início')


        time_end = input(Fore.GREEN + "* Final do corte  (segundos): ")
        # "Final" ERROR TRATAMENT
        error_tratament(time_end, times, 'final')

    return times


def clip_cut(times):
    """Corta o vídeo em determinado período"""

    print(Fore.GREEN + """----------------------------------------------------------

           ==============================
            INICIANDO PROCESSO DE CORTES
           ==============================

----------------------------------------------------------""")
    #importing session

    session(session_name)

    # Clipping raw video
    for index in range(0, len(times) - 1, 2):
        if path.isfile('temp/1.mp4'):
            clip = VideoFileClip("temp/1.mp4")
        else:
            clip = VideoFileClip("temp/1.mkv")

        start = int(times[index])
        end = int(times[index + 1])

        clip = clip.subclip(start, end)
        clip.write_videofile("clips/" + session_name + "/clip_" + str(index + 2) + ".mp4")

def final():
    print(Fore.YELLOW + """----------------------------------------------------------

           ==============================
             !!!CONCLUÍDO COM SUCESSO!!!
           ==============================

----------------------------------------------------------""")

    print(f'* Finalizado. Vá até a pasta {session} em /clips para acessar os cortes.')
