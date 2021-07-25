import os
import settings
import fileinput
import sys



def install(package_name):
    os.system("pip install " + package_name)


def pre_req():
    """Instala dependências"""

    # pytube
    try:
        import pytube
        print("* Módulo pytube está instalado.")
    except ModuleNotFoundError:
        print("\n* Instalando pytube...")
        install("pytube")

    # youtube-dl
    try:
        import youtube_dl
        print("* Módulo youtube-dl está instalado.")
    except ModuleNotFoundError:
        print("\n* Instalando youtube-dl...")
        install("youtube_dl")

    # moviepy
    try:
        import moviepy
        print("* Módulo moviepy já está instalado.")
    except ModuleNotFoundError:
        print("\n* Instalando moviepy...")
        install("moviepy")

    # colorama
    try:
        import colorama
        print("* Módulo colorama já está instalado.")
    except ModuleNotFoundError:
        print("\n* Instalando colorama...")
        install("colorama")
        print()


def install_prereq():

        pre_req()
        for i, line in enumerate(fileinput.input(os.path.join('settings.py'), inplace=1)):
            sys.stdout.write(line.replace('True', 'False'))



if settings.p_req_inst:
    install_prereq()
