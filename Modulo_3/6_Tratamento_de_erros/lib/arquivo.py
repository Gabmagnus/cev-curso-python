from turtle import isvisible
from lib.funçoes import *
from colorama import *


def arquivoExisite(nome):
    #CHECA SE O ARQUIVO EXISTE
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arquivoCriar(nome):
    #CRIA UM ARQUIVO NOVO
    try:
        a = open(nome, 'w+')
        a.close()
    except:
        print(textos('error', 'ao criar o arquivo'))
    else:
        print(f'Arquivo {nome} criado com sucesso')


def arquivoLer(nome):
    #LE O ARQUIVO COMO TXT
    try:
        a = open(nome, 'r')
    except:
        print(textos('error', 'ao criar o arquivo'))
    else:
        f = ''
        lista = a.readlines()
        cabeçalho(f'{Fore.YELLOW}PESSOAS CADASTRADAS{Fore.RESET}')
        print(f'Cód{f:<3}Pessoa{f:<25}Idade')
        for v, c in enumerate(lista, start=1):
            dado = c.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{v:<5} {dado[0]:<30} {dado[1]}')


def arquivoADD(arq, nome, idade):
    #ADCIONA UM PARAMETRO
    try:
        a = open(arq, 'a')
    except:
        print(textos('error', 'ao criar o arquivo'))
    else:
        a.write(f'{nome};{idade}\n')
        a.close()

def arquivoREM(arq, cod):
    try:
        a = open(arq, 'r')
    except:
        print(textos('error', 'ao criar o arquivo'))
    else:
        lista = a.readlines()
        for v, c in enumerate(lista, start=1):
            if v == cod:
                print(c)
                lista.clear()