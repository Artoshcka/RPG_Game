import sys
from battle import *
from hub import *
from logger import *
from storage import *

user, characters = load_data()

characters_hp = [150, 115, 180]
selected_character = 0

def main():
    clear_console()

    global characters, selected_character, user

    if user is None or characters is None:
        user, characters = register_user()
        selected_character = 0

        print(Fore.YELLOW + 'Создан новый пользователь.\n' +
              Fore.CYAN + '  > Давай придумаем никнейм...')

        user.name = input(Fore.WHITE + 'Введите значение: ')
        save_data(user, characters)

    player = characters[selected_character]

    while True:
        action = menu(characters, selected_character, characters_hp)
        if action == 'exit':
            print('Выход из игры...')
            sys.exit()

        elif action == 'select':
            player, selected_character = choose_character(characters, selected_character, user)

        elif action == 'play':
            print(f'\nВы играете за {player.name}!\n')
            fight(player, user)
            continue_()

        elif action == 'profile':
            profile(user)

if __name__ == '__main__':
    main()