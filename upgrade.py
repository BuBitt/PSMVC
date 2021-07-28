#from prereq import *
from shutil import move, copy, rmtree
import requests
import json
import git
import os


upgrade_path = os.path.join('upgrade')
home = os.getcwd()


def check_git():
    try:
        print("-" * 60)
        git = os.system('git --version')
        print('* Buscando Atualizações')
        print()
        return True

    except:
        print("-" * 60)
        print('* Git não instalado, atualizações automáticas não suportadas.')
        print("-" * 60)
        return False


def update_files():
    if os.path.exists(upgrade_path):

        # copiando arquivos
        for stuff in os.scandir(upgrade_path):
            if stuff.is_dir() and stuff.name != 'clips':
                rmtree(os.path.join(home, stuff.name))
                move(os.path.join(upgrade_path, stuff.name), home)
                continue

            if stuff.name != 'clips': 
                copy(stuff.path, home)

        rmtree(upgrade_path)


def upgrade():
    resposta = requests.get('https://api.github.com/repos/BuBitt/PSMVC/commits')
    github_repo = resposta.json()[0]['sha']

    repo = git.Repo(search_parent_directories=True)
    local_repo = repo.head.object.hexsha

    if not local_repo == github_repo:
        print('--- INICIANDO ATUALIZAÇÃO ---')
        os.system('git clone https://github.com/BuBitt/PSMVC.git ' + upgrade_path)
        update_files()
        print("\n* Atualizado com sucesso!")
        print("-" * 60)

    else:
        print(f'* O programa já está no commit: {github_repo[:8]} (Atualizado).')
        print("-" * 60)


if check_git():
    upgrade()
