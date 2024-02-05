class Hangover:
    def __init__(self, max_failures):
        self.max_failures = max_failures
        self.restart_self()

    def add_one_part(self):
        if not self.its_gameover:
            self.alive_parts_counter -= 1
        if self.alive_parts_counter == 0:
            self.its_gameover = True

    def restart_self(self):
        self.alive_parts_counter = self.max_failures
        self.its_gameover = False




if __name__ == '__main__':
    h = Hangover(6)
    while not h.its_gameover:
        print('One step closer to be hanged')
        h.add_one_part()


