from subprocess import Popen
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
    os. system("pip install -r requirements.txt")
    
    if sys.platform.startswith('win32'):
        print('\n------------------------------------------------------------')
        print('* Adicionando ffmpeg ao path do windows.')
        
        p = Popen("win.bat", cwd=r"\\Scripts")
        stdout, stderr = p.communicate()
    
        print("------------------------------------------------------------")



def install_prereq():

        pre_req()
        for i, line in enumerate(fileinput.input(os.path.join('settings.py'), inplace=1)):
            sys.stdout.write(line.replace('True', 'False'))



if settings.p_req_inst:
    install_prereq()
