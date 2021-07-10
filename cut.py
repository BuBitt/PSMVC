from moviepy.editor import *
from colorama import Fore
from os import *
import msgs


times = []


def session_name():
    global s_name
    s_name = input('* Dê um nome à sessão: ')

    return s_name


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
        print('\n' + Fore.GREEN + f'         ------------- Corte Nº {clip_number} -------------')
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
        msgs.no_cuts()       # Import no cuts message

    else:
        msgs.cut_process()    # Imoprt cuts message

    # Clipping raw video
    for index in range(0, len(times) - 1, 2):
        if path.isfile('clips/'+ s_name +'/original/raw.mp4'):
            clip = VideoFileClip("clips/"+ s_name +"/original/raw.mp4")
        else:
            clip = VideoFileClip("clips/"+ s_name +"/original/raw.mkv")

        start = int(times[index])
        end = int(times[index + 1])

        clip = clip.subclip(start, end)
        clip.write_videofile("clips/" + s_name + "/clip_" + str(index + 2) + ".mp4")
