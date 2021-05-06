import os
import random
import platform


def get_a_random_word(level):
    words = []

    if level == 1:
        evaluation = range(3, 6)
    elif level == 2:
        evaluation = range(6, 10)
    elif level == 3:
        evaluation = range(10, 30)
    else:
        raise ValueError("Nivel no definido.")

    try:
        with open("./data/words.txt", 'r', encoding='utf8') as file:
            words = list(map(lambda line: line.replace('\n', ''), file.readlines()))
            words = [word for word in words if len(word) in evaluation]
    except FileNotFoundError:
        print('El archivo data/words.txt no se encuentra')
        exit()

    return random.choice(words)


def normalize_word(word):
    new_word = []
    vocals = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}

    for letter in word:
        if letter in vocals.keys():
            new_word.append(vocals[letter])
        else:
            new_word.append(letter)

    return "".join(new_word).lower()


def print_word(word, letters):
    normalized_word = normalize_word(word)
    new_word = list(map(lambda letter: letter if letter in letters else "_", normalized_word))

    print('\n')
    print(" ".join(new_word).upper())
    print('\n')
    print(f'La palabra consta de {len(word)} letras.')
    print("=" * 50)


def print_lives(lifes):
    print(f'Te quedan {"♥ " * lifes}({lifes}) vidas.')
    print("=" * 50)


def print_letters(letters):
    print(f'Has usado las letras: {", ".join(letters)}')
    print("=" * 50)


def check_letter(word, letter):
    normalized_word = normalize_word(word)
    return letter in normalized_word


def check_word(word, letters):
    normalized_word = normalize_word(word)
    all_letters = list(map(lambda letter: letter in letters, normalized_word))
    return all(all_letters)


def clean_console():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')


def main():
    letters = []
    menu = '''

    █████╗ ██╗  ██╗ ██████╗ ██████╗  ██████╗ █████╗ ██████╗  ██████╗
    ██╔══██╗██║  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗
    ███████║███████║██║   ██║██████╔╝██║     ███████║██║  ██║██║   ██║
    ██╔══██║██╔══██║██║   ██║██╔══██╗██║     ██╔══██║██║  ██║██║   ██║
    ██║  ██║██║  ██║╚██████╔╝██║  ██║╚██████╗██║  ██║██████╔╝╚██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝


        1. Fácil     (4 a 5 letras)
        2. Dificil   (6 a 9 letras)
        3. Erudito   (10 a más letras)
    '''

    game_over = '''

    ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
    ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
    ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
    ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
    ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
    ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
    ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
        ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                        ░

    '''

    continue_playing = True

    while continue_playing:
        print(menu)
        print("=" * 80)

        level = int(input('Escoge el nivel de dificultad: '))
        word = get_a_random_word(level)
        lives = level * 5

        clean_console()

        while True:
            print_lives(lives)
            print_word(word, letters)
            print_letters(letters)

            character = input('Ingresa una letra: ')
            if character in letters:
                clean_console()
                print(f'El caracter {character} ya ha sido usado, prueba con otro.')
                print('\n')
                continue

            letters.append(character)

            if not check_letter(word, character):
                lives -= 1

            result_check_word = check_word(word, letters)

            if result_check_word or lives == 0:
                if lives == 0:
                    print(game_over)
                    print(f'La palabra era: {word.upper()}.')
                elif result_check_word:
                    print('\n')
                    print(f'Felicidades adivinaste la palabra {word.upper()}.')

                print('\n')
                continue_playing = input('Desea seguir jugando? si/no ') == 'si'
                letters.clear()
                clean_console()
                break

            clean_console()


if __name__ == "__main__":
    main()
