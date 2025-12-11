import os
from time import sleep
from main import *
from colorama import *

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def error():
    clear_console()
    print('Упс... Ошибочка!')
    sleep(1)
    clear_console()

def continue_():
    input(Fore.BLUE + 'Нажмите ENTER чтобы вернуть в меню...')
    clear_console()
    input(Fore.BLUE + 'Нажмите ENTER ещё раз...')
