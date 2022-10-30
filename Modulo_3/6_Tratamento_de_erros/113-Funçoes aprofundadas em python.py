from colorama import *
def textos(n):
    if n == 'op_inv':
        return f'{Fore.RED}A opçao que você digitou nao é valida!{Fore.RESET}'
    elif n == 'op_int_us':
        return f'{Fore.RED}Operaçao interrompida pelo usuário\nO Programa sera finalizado{Fore.RESET}'
def intcheck(num):
    while True:
        try:
            n = int(input(num).strip())
        except (ValueError, TypeError):
            print(textos('op_inv'))
            continue
        except KeyboardInterrupt:
            print(textos('op_int_us'))
            return 0
            end
        else:
            return n
            break


def floatcheck(num):
    while True:
        try:
            n = float(input(num).strip())

        except (ValueError, TypeError):
            print(textos('op_inv'))
            continue

        except KeyboardInterrupt:
            print('A ação foi interrompida pelo usuário, a escolha padrão será 0')
            return 0.0

        else:
            return float(n)
            break


ni = intcheck('Digite um INTEIRO: ')
nr = floatcheck('Digite um REAL: ')

print(f'O Valor inteiro digitado foi {ni} e o valor real foi {nr}')