class Opponent:
    def __init__(self, word_pool: list):
        self.make_a_word(word_pool)

    def make_a_word(self, word_pool):
        import random
        self.word = random.choice(word_pool)

    def tell_positions_of_char(self, char):
        positions = []
        for i in range(len(self.word)):
            if self.word[i] == char:
                positions.append(i)
        return positions
