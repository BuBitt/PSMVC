from colorama import *
import cut


def line():
    return print("------------------------------------------------------------")


def no_cuts():
    print("""------------------------------------------------------------
* Não há cortes
------------------------------------------------------------""")


def cut_process():
    print(Fore.GREEN + """------------------------------------------------------------

             ==============================
              INICIANDO PROCESSO DE CORTES
             ==============================
""")


def final():
    print(Fore.YELLOW + """------------------------------------------------------------

             ==============================
              !!!CONCLUÍDO COM SUCESSO!!!
             ==============================

------------------------------------------------------------""")

    print('* Vá até a pasta ' + Fore.BLUE + f'/clips/{cut.s_name}' + Fore.YELLOW + ' para acessar os cortes.')
    print('------------------------------------------------------------')


def dependences():
    print("""
------------------------------------------------------------

             ================================
              ANÁLISE DE DEPENDÊNCIAS PSMVC
             ================================

------------------------------------------------------------""")


def downloader():
    print(Fore.BLUE + """------------------------------------------------------------

           ================================
            INICIANDO PROCESSO DE DOWNLOAD
           ================================
""")


def select_cuts():
    print(Fore.GREEN + """------------------------------------------------------------

             ==============================
                   SELEÇAO DE CORTES
             ==============================
""")
