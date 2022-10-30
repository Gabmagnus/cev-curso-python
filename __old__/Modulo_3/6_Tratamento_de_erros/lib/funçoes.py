from time import sleep
from colorama import *
import os


def clean():
    #LIMPAR CMD
    os.system('cls')


def textos(n, rest=''):
    #TEXTOS PREDEFINIDOS!
    if n == 'error':
        print('Ocorreu um erro ', rest)
    if n == 'val_inv':
        print(f'{Fore.RED}O Valor que voce digitou não é valido!{Fore.RESET}')
    elif n == 'op_inv':
        print(f'{Fore.RED}A opçao que você digitou nao é valida!{Fore.RESET}')
    elif n == 'op_int_us':
        print(f'{Fore.RED}Operaçao interrompida pelo usuário\nO Programa sera finalizado{Fore.RESET}')


def checkint(txt):
    #CHECANDO SE É INT
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            textos('val_inv')
            continue
        except KeyboardInterrupt:
            textos('op_int_us')
            return 3
            break
        else:
            return n
            break


def linha():
    #FAZER LINHA
    print('~'*40)


def cabeçalho(t):
    #CABEÇALHO BONITO
    print('~'*40)
    print(str(t).center(40))
    print('~'*40)


def menu(l):
    #MENU PRINCIPAL EM FORMATO DE LISTA
    clean()
    cabeçalho(f'{Fore.YELLOW}MENU PRINCIPAL{Fore.RESET}')
    for n, item in enumerate(l, start=1):
        print(f'{Fore.GREEN}{n: <2} {Fore.RESET} {Fore.YELLOW}{item}{Fore.RESET}')
    linha()
    opç = checkint(f'{Fore.GREEN}Digite sua opção » {Fore.YELLOW}')
    return opç