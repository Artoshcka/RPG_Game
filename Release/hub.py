from main import *
from classes import *
from storage import *
from logger import *
from colorama import *

def menu(characters, selected_character, characters_hp):
    clear_console()

    for char in range(len(characters)):
        characters[char].hp = characters_hp[char]

    while True:
        print(Fore.GREEN + '<-' + '='*5 + ' МЕНЮ ' + '='*5 + '->\n')
        print(Fore.WHITE + '1) Играть\n'
            '2) Выбрать персонажа\n' +
            Fore.YELLOW + f'   -> Выбран: {characters[selected_character].name}\n' +
            Fore.WHITE + '3) Профиль\n' +
            Fore.RED + '\nx) Выход из игры\n')

        option = input(Fore.WHITE + "Выбрано: ").lower()

        if option == '1':
            return 'play'
        elif option == '2':
            return 'select'
        elif option == '3':
            return 'profile'
        elif option == 'x':
            return 'exit'
        else:
            error()

def profile(user):
    clear_console()

    while True:
        print(Fore.GREEN + '<-' + '=' * 5 + ' ПРОФИЛЬ ' + '=' * 5 + '->\n')
        visual_coins = VisualCoins(user.coins)

        print(Fore.YELLOW + f'Имя: {user.name}\n' +
              Fore.WHITE + f'-'*(len(user.name) + 5) +
                           f'\nМонеты: ' + Fore.GREEN + str(visual_coins) + '' +
              Fore.RED + '\n\nx) Выход в меню' + Fore.WHITE)

        option = input('\nВыбрано: ')

        if option == 'x':
            return 'exit'
        else:
            error()

def choose_character(characters, selected_character, user):
    clear_console()

    print(Fore.BLUE + '\nВыберите персонажа:\n')
    for i, char in enumerate(characters):
        if characters[i].unlocked:
            status = Fore.GREEN +  '( Разблокирован )'
        else:
            status = Fore.RED + f'( Заблокирован ) ---> ' + Fore.CYAN + f'Купить за {char.price} монет' + Fore.WHITE

        print(Fore.YELLOW + f'({i+1}) ' + Fore.WHITE + f'{char.name} {status}' + Fore.WHITE +
            f'\nЗдоровье: {char.hp}\n'
            f'Урон: {char.attack}\n'
            f'Защита: {char.defense}\n')
        print('<-' + '='*15 + '->\n')

    while True:
        choice = input('\nВыбрано: ')

        if characters[int(choice) - 1].unlocked:
            selected_character = int(choice) - 1

        else:
            clear_console()
            print(Fore.RED + '> Выбранный персонаж заблокирован !')

            if user.coins >= characters[int(choice) - 1].price:
                buy_character(characters, choice, user)
            else:
                print(Fore.YELLOW + f'--> Вам не хватает: {(user.coins - characters[int(choice) - 1].price) * -1} монет.\n')
                continue_()

        if choice.isdigit() and 1 <= int(choice) <= len(characters):
            return characters[selected_character], selected_character
        else:
            print('Неверный ввод, попробуйте снова.')

def buy_character(characters, choice, user):
    try:
        choice = int(choice) - 1
    except ValueError:
        error()
    else:
        print(Fore.YELLOW + f'> Вы можете приобрести {characters[choice].name}\n'
                            f'  за {characters[choice].price} монет.\n\n'
                            f'{Fore.GREEN}Купить - Y {Fore.WHITE}|{Fore.RED} Отмена - X')
        answer = input(Fore.WHITE + '\nВыбрано: ')

        if answer.lower() == 'y':
            characters[choice].unlocked = True
            user.coins -= characters[choice].price

            save_data(user, characters)

            clear_console()
            visual_coins = VisualCoins(user.coins)

            print(Fore.YELLOW + 'Персонаж разблокирован !\n' +
                  Fore.CYAN + f'Текщий баланс: {visual_coins} монет.\n')
            continue_()

        elif answer.lower() == 'x':
            clear_console()
            print(Fore.RED + 'Покупка отменена !')
            continue_()

def register_user():
    user = User('Пустое имя', 100, False)
    characters = [
        Character('Викинг', 0, 25, 20, True, 0),
        Character('Лучник', 0, 45, 10, False, 1000),
        Character('Маг', 0, 15, 25, False, 2500)
    ]

    save_data(user, characters)
    return user, characters

    continue_()