import argparse


import urllib
import urllib.request

while True: 
    try:
        site = urllib.request.urlopen('https://youtube.com')
    except (UnicodeError, urllib.error.URLError):
        print(f'Algo deu errado!')
        break
    else:
        print('Tudo OK!!!')