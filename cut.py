from posix import listdir
from moviepy.editor import VideoFileClip
from colorama import Fore
from os import chdir, getcwd, path
import msgs


times = []


def session_name():
    global s_name
    s_name = input('* Dê um nome à sessão: ')

    return s_name


def times_input():
    """Coleta e salva os tempos para os cortes"""

    clip_number = 0
    error = False


    while 1:
        try:
            clip_number += 1
            
            if error:
                print('\n' + Fore.RED + erro_msg)
                print(f'         ------------- Corte Nº {clip_number} -------------')
            
            else:
                print('\n' + Fore.GREEN)
                print(f'         ------------- Corte Nº {clip_number} -------------')
            
            time_init = input("* Início do corte (segundos): ")

            if time_init == '':
                break

            if not time_init.isdigit():
                raise ValueError('\n!!! Erro: Digite um número válido (inteiro).')

            time_end = input("* Final do corte  (segundos): ")
            if not time_end.isdigit():
                raise ValueError('\n!!! Erro: Digite um número válido (inteiro).')

            error = False
            
            if time_init > time_end or time_init == time_end:
                raise ValueError('\n!!! Erro: Valor final maior ou igual o inicial.')

        except ValueError as err:
            if clip_number < 0:
                clip_number = 1
            else:
                clip_number -= 1

            erro_msg = str(err)            
            error = True
            pass
        
        except KeyboardInterrupt:
            print('\nBye Bye')
            quit()
        
        else:
            times.append(int(time_init))
            times.append(int(time_end))
        
    return times


def clip_cut(times):
    """Corta o vídeo em determinado período"""
    
    cl = 0
    t_times = []

    if times == t_times:
        msgs.no_cuts()  # Import no cuts message

    else:
        msgs.cut_process()  # Imoprt cuts message


    # Clipping raw video
    for index in range(0, len(times) - 1, 2):
        cl += 1
        file_path = path.join(getcwd(), 'clips', s_name, 'original')
        file_name = listdir(file_path)[0]
        
        clip = VideoFileClip(path.join(file_path, file_name))

        start = int(times[index])
        end = int(times[index + 1])

        clip = clip.subclip(start, end)
        clip.write_videofile(path.join('clips', s_name, "clip_" + str(cl + 1) + ".mp4"))

