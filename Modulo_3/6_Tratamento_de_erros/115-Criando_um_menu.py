from mailbox import NotEmptyError
from time import sleep
from colorama import *
from lib.funçoes import *
from lib.arquivo import *
from tkinter import * 



#GERADOR DE ARQUIVO
if not arquivoExisite('DB.txt'):
    arquivoCriar('DB.txt')
#GERADOR DE ARQUIVO

while True:
    res = menu(['Ver Pessoas cadastradas', 'Cadastrar novo integrante', 'Deletar integrante', 'Sair do programa'])
    print(Fore.RESET)
    if res == 1:
        #VER PESSOAS CADASTRADAS
        clean()
        arquivoLer('DB.txt')
        input("Press Enter to continue...")

    elif res == 2:
        #CADASTRAR NOVO INTEGRANTE
        clean()
        cabeçalho(f'{Fore.YELLOW}CADASTRO{Fore.RESET}')
        arquivoADD('DB.txt', input('Nome » '), checkint('Idade » '))
        print(f'{Fore.GREEN}Cadastrando.... {Fore.RESET}')
        sleep(2)

    elif res == 3:
        clean()
        arquivoREM('DB.txt', int(input('Código do usuário removido: ')))
        sleep(2)

    elif res == 4:
        #SAIR DO PROGRAAM
        clean(1)
        print(f'{Fore.RED}Você escolheu sair do programa!\ntodos os dados foram salvos\nObrigado!{Fore.RESET}')
        break
        sleep(2)

    else:
        #OPÇ INVALIDA
        print(textos('op_inv'))
        sleep(2)
        clean()




