import random
from main import *
from classes import *
from colorama import *
from logger import *


def fight(player, user):
    random_hp = [50, 100, 150, 220]
    random_attack = [10, 25, 50, 75, 150]
    random_defense = [0, 5, 10, 15]
    random_name = ['Ведьма', 'Гоблин', 'Скелеты', 'Злодей-Шмакодявка']

    clear_console()

    selected_enemy = Enemy(random.choice(random_name), random.choice(random_hp), random.choice(random_attack), random.choice(random_defense))

    print(f'\n На вас напал(-а, -и) {selected_enemy.name}!\n')

    while player.is_alive() and selected_enemy.is_alive():

        print(f'{player.name}: {player.hp} HP | {selected_enemy.name}: {selected_enemy.hp} HP')
        input(Fore.YELLOW + ' --> Нажмите ENTER чтобы атаковать...' + Fore.WHITE)

        damage = player.attack
        selected_enemy.hp -= damage - damage * (selected_enemy.defense/100)
        print(f'\nВы нанесли {damage} урона!')

        if not selected_enemy.is_alive():
            random_coins = [50, 150, 200, 250, 5000]
            add_coin = random.choice(random_coins)
            user.coins += add_coin

            save_data(user, characters)
            clear_console()

            print(Fore.GREEN + 'Победа! Вы убили монстра!\n\n' +
                Fore.CYAN + f'Награды: \n'
                            f' > Монеты: + {add_coin}')

            return

        damage = selected_enemy.attack
        player.hp -= damage - damage * (player.defense/100)
        print(f'Монстр нанес вам {damage} урона!\n')

        if not player.is_alive():
            clear_console()

            print(Fore.RED + 'Вы погибли...\n')
            return