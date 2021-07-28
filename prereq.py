from subprocess import Popen
from msgs import 
import fileinput
import settings
import sys
import os



def install(package_name):
    os.system("pip install " + package_name)


def pre_req():
    """Instala dependências"""
    print("""
------------------------------------------------------------

             ================================
              ANÁLISE DE DEPENDÊNCIAS PSMVC
             ================================

------------------------------------------------------------""")
    os.system("pip install -r requirements.txt")
    print("------------------------------------------------------------")



def install_prereq():

        pre_req()
        with open('settings.py', 'w') as stt:
            stt.write('p_req_inst = False')




if settings.p_req_inst:
    install_prereq()
