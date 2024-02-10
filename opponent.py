class Opponent:
    def __init__(self, word_pool):
        self.word_pool = word_pool
        self.make_a_word(word_pool)
        self.guessed_chars = set()
        self.word_is_guessed = False

    def make_a_word(self, word_pool):
        import random
        self.word = random.choice(word_pool)

    @staticmethod
    def check_if_char_is_present(func):
        def checker(self, char):
            if char in self.word:
                self.guessed_chars.add(char)
            return func(self, char)
        return checker

    @staticmethod
    def check_if_all_guessed(func):
        def checker(self, *args):
            if set(self.word) == self.guessed_chars:
                self.word_is_guessed = True
            return func(self, *args)
        return checker

    @check_if_char_is_present
    @check_if_all_guessed
    def tell_positions_of_char(self, char):
        positions = []
        for i in range(len(self.word)):
            if self.word[i] == char:
                positions.append(i)
        return positions

    def restart(self):
        self.make_a_word()
        self.word_is_guessed = False
        self.guessed_chars = set()


if __name__ == '__main__':
    opp = Opponent(['оса', 'коса', 'сосиска'])
    print(opp.tell_positions_of_char('с'))
    opp.tell_positions_of_char('о')
    opp.tell_positions_of_char('к')
    opp.tell_positions_of_char('и')
    opp.tell_positions_of_char('а')
    print(opp.word)
    print(opp.guessed_chars)
    print(opp.word_is_guessed)



