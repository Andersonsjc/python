# -*- coding: UTF-8 -*-
#JOGO DA FORCA#
import random
from linecache import getline
import re

def start():
    print ('========== JOGO DA FORCA ==========')
    print('')
    local = 'c:/Users/andesiqu/OneDrive - Embraer/python/MySamples/'
    file_words = f'{local}hangman_words.txt'
    word = get_word(file_words)
    array_letter = []
    array_hangman = []
    letter = ' '
    tent = 0

    while True:
        hangman_step(tent)
        array_hangman = array_word(word, array_letter, tent)
        print(f'Palavra = {array_hangman}')
        if not '_' in array_hangman:
            print(f'Parabéns!!!')
            func_continue()
        if tent == 6:
            print(f'Não foi dessa vez! Palavra correta: {word.upper()}')
            func_continue()

        print(f'Letrar digitadas: {array_letter}')
        letter = ask_letter(array_letter)
        if letter not in word:
            tent += 1
        array_letter.append(letter.upper())
        
def func_continue():
    option = input('Deseja jogar novamente? y/n ')
    if option not in ('y','n'):
        func_continue()
    elif option == 'y':
        start()
    else:
        exit()

def get_word(file_words):
    with open(file_words,'r') as fileword:
        lines_qtd = len(fileword.readlines())
        fileword.seek(0)
        num_ramd = random.randint(0,lines_qtd-1)
        word = fileword.readlines()[num_ramd].strip()
        #print(f'word = {word}')
        return word    

def count_letter(letter):
    if not(len(letter) == 1):
        print('Favor digitar apenas uma letra!')
        return True
    else:
        False

def ask_letter(array_letter):
    while True:
        letter = input('Digite uma letra: ')
        if letter.upper() in array_letter:
            print('Essa letra já foi digitada, escolha outra')
            continue
        elif not(len(letter) == 1):
            print('Favor digitar apenas uma letra!')
            continue
        elif re.search(r'[^a-zA-Z]', letter):
            print('Favor digitar um letra')
            continue
        else:
            break

    return letter

def array_word(word, array_letter, tent):
    array_word = []
    for letter in word:
        if letter.upper() in array_letter:
            array_word.append(letter.upper())
        else:
            array_word.append('_')
    return array_word

def hangman_step(erro_index):
    list_hang = [
"""            ----------
            |        |
                     |
                     |
                     |
                     |
                     |
                     |
        ------------------            
            """,
"""            ----------
            |        |
            O        |
                     |
                     |
                     |
                     |
                     |
        ------------------            
            """,
"""            ----------
            |        |
            O        |
            |        |
                     |
                     |
                     |
                     |
        ------------------            
            """,
"""            ----------
            |        |
            O        |
           /|        |
                     |
                     |
                     |
                     |
        ------------------            
            """,
"""            ----------
            |        |
            O        |
           /|\       |
                     |
                     |
                     |
                     |
        ------------------            
            """,
"""            ----------
            |        |
            O        |
           /|\       |
           /         |
                     |
                     |
                     |
        ------------------            
            """,
"""            ----------
            |        |
            O        |
           /|\       |
           / \       |
                     |
        ------------------            
            """   
    ]
    print(list_hang[erro_index])

def end_game():
    pass


if __name__ == "__main__":
    start()