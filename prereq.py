import os


def install(package_name):
    os.system("pip install " + package_name)


def pre_req():
    """Instal dependências"""
    # youtube-dl
    try:
        import youtube_dl
        print("Módulo youtube-dl está na máquina.")
    except ModuleNotFoundError:
        print("Instalando youtube-dl...")
        install("youtube_dl")

    # moviepy
    try:
        import moviepy
        print("Módulo moviepy já está Instalado.")
    except ModuleNotFoundError:
        print("Instalando moviepy...")
        install("moviepy")

    # colorama
    try:
        import colorama
        print("Módulo colorama já está instalado.")
    except ModuleNotFoundError:
        print("Instalando colorama...")
        install("colorama")
