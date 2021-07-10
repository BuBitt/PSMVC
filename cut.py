from moviepy.editor import *
from colorama import Fore
from os import *


times = []


def session_name():
    global s_name
    s_name = input('* Dê um nome à sessão: ')
    print("----------------------------------------------------------")
    return s_name


def session(session_name):
    #os.mkdir("temp/" + s_name)
    os.mkdir("clips/" + s_name)


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

    t_times = []

    if times == t_times:
        print(Fore.GREEN + """----------------------------------------------------------
* Não há cortes
----------------------------------------------------------""")

    else:
        print(Fore.GREEN + """----------------------------------------------------------

           ==============================
            INICIANDO PROCESSO DE CORTES
           ==============================

----------------------------------------------------------""")
    # Importing session
    # session(s_name)

    # Clipping raw video
    for index in range(0, len(times) - 1, 2):
        if path.isfile('clips/'+ s_name +'/original/raw.mp4'):
            clip = VideoFileClip("clips/"+ s_name +"/1 raw.mp4")
        else:
            clip = VideoFileClip("clips/"+ s_name +"/1 raw.mkv")

        start = int(times[index])
        end = int(times[index + 1])

        clip = clip.subclip(start, end)
        clip.write_videofile("clips/" + s_name + "/clip_" + str(index + 2) + ".mp4")

def final():
    print(Fore.YELLOW + """----------------------------------------------------------

           ==============================
             !!!CONCLUÍDO COM SUCESSO!!!
           ==============================

----------------------------------------------------------""")

    print(f'* Finalizado. Vá até a pasta ' + Fore.BLUE + f'/{s_name}' + Fore.YELLOW + ' em '+ Fore.BLUE +'/clips' + Fore.YELLOW + ' para acessar os cortes.')
