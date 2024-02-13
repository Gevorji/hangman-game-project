import json
import os
import sys
from functools import partial
import time
from hangover import Hangover
from opponent import Opponent
from table import Table

russian_alphabet = [chr(i) for i in range(1072, 1104)]


def process_frames(file):
    frame_source = file.readlines()
    frames = []
    frame = []
    for line in frame_source:
        if line == 'delim\n':
            frame = ''.join(frame)
            frames.append(frame)
            frame = []
        else:
            frame.append(line)
    return frames


def remember_char_if_is_entered_first(checker, entered_chars):

    def checker_wrapper(char):
        is_entered = checker(char, entered_chars)
        if is_entered:
            entered_chars.append(char)
        return is_entered

    return checker_wrapper


def is_in_collection(item, collection):
    return item in collection


def is_not_in_collection(item, collection):
    return item not in collection


def get_valid_input(validators, invite_msg, msgs_if_not_valid, on_frame_change):
    msgs_if_not_valid = {validator: msg for validator, msg in zip(validators, msgs_if_not_valid)}
    char = input(invite_msg).casefold()
    is_valid = False
    while not is_valid:
        for validator in validators:
            if not validator(char):
                break
        else:
            is_valid = True
            break
        on_frame_change()
        char = input(msgs_if_not_valid[validator]).casefold()
    return char


def make_frame_changer(*components):
    components = list(components)

    def change_frame(*pargs, msg_part=None):
        os.system('cls')
        frame = components[:-1] + [msg_part] + components[-1:] if msg_part else components
        for frame_component in frame:
            if hasattr(frame_component, 'display'):
                print(frame_component.display())
            else:
                print(frame_component)
    return change_frame


def end():
    import sys
    sys.exit()


def main():
    os.system('cls')
    word_pool = json.load(open('russian_nouns_prepared.json', encoding='utf-8'))
    word_pool = ['къуайса']
    animation_frames = open('body_art.txt', encoding='utf-8')
    hangover = Hangover(6, process_frames(animation_frames))
    opponent = Opponent(word_pool)
    table = Table(len(opponent.word))
    entered_chars = []
    frame_changer = make_frame_changer(hangover, table)
    frame_changer(msg_part='Lets go\n')

    while not opponent.word_is_guessed:
        validators = [partial(is_in_collection, collection=russian_alphabet),
                      remember_char_if_is_entered_first(is_not_in_collection, entered_chars)]
        char = get_valid_input(validators, 'Enter a character: ',
                               ('You\'ve entered wrong character. Only russian alphabet is valid. Try again: ',
                                'You have already entered this character. Enter something new what: '),
                               frame_changer)
        char_positions = opponent.tell_positions_of_char(char)
        if char_positions:
            for position in char_positions:
                table.put_a_char(char, position)
            frame_changer(msg_part='You were right!')
        else:
            hangover.add_one_part()
            if hangover.its_gameover:
                win = False
                break
            else:
                frame_changer(msg_part=f'Well there is no "{char}" in that word!')
    else: win = True
    match win:
        case True:
            frame_changer(msg_part='You win! Would you like to restart? (y/n)')
            answer = get_valid_input([partial(is_in_collection, collection=['y', 'n'])],
                                     '','Try again (y/n): ', frame_changer)
        case False:
            frame_changer(msg_part='You lost! But you can try again though! (y/n): ')
            answer = get_valid_input([partial(is_in_collection, collection=['y', 'n'])],
                                     '', 'Try again (y/n): ', frame_changer)
    match answer:
        case 'y':
            restart = True
        case 'n':
            restart = False

    return restart


if __name__ == '__main__':
    os.system('cls')
    answer = get_valid_input([partial(is_in_collection, collection=['y', 'n'])],
                             '''I welcome you at the game of Hangover!
Please type (y/Y) if you want to begin and (n/N) to quit: ''',
                             ['Try again (y/n): '], make_frame_changer())
    match answer:
        case 'y':
            try:
                restart = main()
            except:
                raise
        case 'n':
            quit()
    while restart:
        restart = main()
