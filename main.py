import json
import os
import time
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
    word_pool = ['къуайса']
    animation_frames = open('body_art.txt', encoding='utf-8')
    hangover = Hangover(6)
    opponent = Opponent(word_pool)
    hang_drawer = Drawer(animation_frames)
    table = Table(len(opponent.word))
    hang_drawer.draw_a_frame()
    entered_chars = []
    print('Lets go\n', table.display())

    while not opponent.word_is_guessed:
        char = input('Enter a character:')
        while not is_valid_string(char.casefold(), russian_alphabet):
            os.system('cls')
            hang_drawer.draw_a_frozen_frame()
            print(table.display())
            char = input('You\'ve entered wrong character. Only russian alphabet is valid. Try again: ')
        while char in entered_chars:
            hang_drawer.draw_a_frozen_frame()
            print(table.display())
            char = input(f'You already entered character "{char}"\nEnter something different: ')
        entered_chars.append(char)
        char_positions = opponent.tell_positions_of_char(char)
        if char_positions:
            os.system('cls')
            hang_drawer.draw_a_frozen_frame()
            for position in char_positions: table.put_a_char(char, position)
            print('You were right!')
            print(table.display())
        else:
            hangover.add_one_part()
            hang_drawer.draw_a_frame()
            if hangover.its_gameover:
                win = False
                answer = input('You\'ve lost unfortunately... You can try again though! (y/n): ')
                match answer.casefold():
                    case 'y':
                        main()
                    case 'n':
                        quit()
            else:
                print(f'Well there is no "{char}"s in that word!')
                print(table.display())
    win = True
    match win:
        case True:
            os.system('cls')
            hang_drawer.draw_a_frozen_frame()
            print(table.display())
            answer = input('You win! Would you like to restart? (y/n)')
            while not is_valid_string(answer.casefold(), ['y', 'n']):
                os.system('cls')
                hang_drawer.draw_a_frozen_frame()
                print(table.display())
                answer = input('Try again (y/n): ')
            match answer:
                case 'y':
                    restart = True
                case 'n':
                    restart = False
        case False:
                os.system('cls')
                hang_drawer.draw_a_frozen_frame()
                print(table.display())
                answer = input('You lost! But you can try again though! (y/n): ')
                while not is_valid_string(answer.casefold(), ['y', 'n']):
                    os.system('cls')
                    hang_drawer.draw_a_frozen_frame()
                    print(table.display())
                    answer = input('Try again (y/n): ')
                match answer:
                    case 'y':
                        restart = True
                    case 'n':
                        restart = False

    return restart




def on_start():
    os.system('cls')
    answer = input('I welcome you at the game of Hangover! Please type (y/Y) if you want to begin and (n/N) to quit: ')
    while True:
        if not is_valid_string(answer.casefold(), ['y', 'n']):
            answer = input('Try again:')
        else:
            match answer.casefold():
                case 'y':
                    restart = main()
                    break
                case 'n': quit()
    return restart

if __name__ == '__main__':
    restart = on_start()
    while restart:
        restart = main()

