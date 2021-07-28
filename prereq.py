from subprocess import Popen
import fileinput
import settings
import sys
import os


def pre_req():
    """Instala dependências"""
    print("""
------------------------------------------------------------

             ================================
              ANÁLISE DE DEPENDÊNCIAS PSMVC
             ================================

------------------------------------------------------------""")


def install_prereq():
    pre_req()
    with open('settings.py', 'w') as stt:
        stt.write('p_req_inst = False')

    os.system("pip install -r requirements.txt")
    print("-" * 60)


if settings.p_req_inst:
    install_prereq()
