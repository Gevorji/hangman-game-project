import json
import os
from hangover import Hangover
from opponent import Opponent
from drawer import Drawer
from table import Table

russian_alphabet = [chr(i) for i in range(1072, 1104)]

def is_valid_string(strg, appropriate):
    if strg in appropriate:
        return True
    else:
        return False

def end():
    import sys
    sys.exit()

def main():
    os.system('cls')
    word_pool = json.load(open('russian_nouns_prepared.json', encoding='utf-8'))
    animation_frames = open('body_art.txt', encoding='utf-8')
    hangover = Hangover(6)
    opponent = Opponent(word_pool)
    hang_drawer = Drawer(animation_frames)
    table = Table(len(opponent.word))
    hang_drawer.draw_a_frame()
    print('Lets go\n', table.display())

    while not opponent.word_is_guessed:
        char = input('Enter a character:')
        while True:
            if not is_valid_string(char.casefold(), russian_alphabet):
                char = input('You\'ve entered wrong character. Only russian alphabet is valid. Try again: ')
            else: break
        char_positions = opponent.tell_positions_of_char(char)
        if char_positions:
            hang_drawer.draw_a_frame()
            for position in char_positions: table.put_a_char(char, position)
            print('You were right!')
            print(table.display())
        else:
            hangover.add_one_part()
            hang_drawer.draw_a_frame()
            if hangover.its_gameover():
                answer = input('You\'ve lost unfortunately... You can try again though! (y/n): ')
                match answer.casefold():
                    case 'y':
                        main()
                    case 'n':
                        quit()
            else:
                print(f'Well there is no "{char}"s in that word!')
                print(table.display())




answer = input('I welcome you at the game of Hangover! Please type (y/Y) if you want to begin and (n/N) to quit: ')
while True:
    if not is_valid_string(answer.casefold(), ['y', 'n']):
        answer = input('Try again:')
    else:
        match answer.casefold():
            case 'y': main()
            case 'n': quit()
        quit()

