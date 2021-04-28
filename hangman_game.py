import os
import random

def get_a_word(words):
    return random.choice(words)

def read_words_file(level):
    words = []

    if level == 1:
        evaluation = [ 4, 5 ]
    elif level == 2:
        evaluation = [ 6 ]
    elif level == 3:
        evaluation = [ 7, 8]
    else:
        raise ValueError("Nivel no definido.")

    with open("./data/words.txt", 'r') as file:
        words = list(map(lambda line: line.replace('\n', ''), file.readlines()))
        words = [word for word in words if len(word) in evaluation]

    return words

def normalize_word(word):
    new_word = []
    vocals = { 'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u' }

    for letter in word:
        if letter in vocals.keys():
            new_word.append(vocals[letter])
        else:
            new_word.append(letter)

    return "".join(new_word).lower()

def print_word(word, letters):
    normalized_word = normalize_word(word)
    new_word = list(map(lambda letter: letter if letter in letters else "_", normalized_word))

    print('¡Adivina la palabra!')
    print('\n')
    print(" ".join(new_word).upper())
    print('\n')

def check_word(word, letter):
    return False

def clean_window():
    os.system('clear')

def main():
    letters = []
    intentos_fallidos = 0
    menu = '''

        _|    _|    _|_|    _|      _|    _|_|_|  _|      _|    _|_|    _|      _|
        _|    _|  _|    _|  _|_|    _|  _|        _|_|  _|_|  _|    _|  _|_|    _|
        _|_|_|_|  _|_|_|_|  _|  _|  _|  _|  _|_|  _|  _|  _|  _|_|_|_|  _|  _|  _|
        _|    _|  _|    _|  _|    _|_|  _|    _|  _|      _|  _|    _|  _|    _|_|
        _|    _|  _|    _|  _|      _|    _|_|_|  _|      _|  _|    _|  _|      _|

        1. Fácil     (4 a 5 letras)
        2. Dificil   (6 letras)
        3. Erudito   (7 a 8 letras)
    '''

    print(menu)
    print("=" * 100)

    level = int(input('Escoge el nivel de dificultad: '))

    print('Cargando palabras...')
    words = read_words_file(level)
    print('Escogiendo una palabra al hazar...')
    word = get_a_word(words)
    clean_window()

    while True:
        print_word(word, letters)
        character = input('Ingresa una letra: ')
        letters.append(character)

        if check_word(word, letters) or len(letters) >= 5:
            break

        clean_window()

    if len(letters) >= 5:
        print('Game over :\'C')
    else:
        print('Felicidades adivinaste la palabra.')

if __name__ == "__main__":
    main()
