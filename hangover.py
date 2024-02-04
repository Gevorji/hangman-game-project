class Hangover:
    body_art = open('body_art.txt', encoding='utf-8').readlines()
    def __init__(self):
        self.process_frames()
        self.restart()

    def draw_a_part(self):
        try:
            return next(self.frame_producer)
        except StopIteration:
            self.game_over= True

    def restart(self):
        self.frame_producer = (frame for frame in self.frames)
        self.game_over = False
    def process_frames(self):
        self.frames = []
        frame = []
        for line in self.body_art:
            if line == 'delim\n':
                frame = ''.join(frame)
                self.frames.append(frame)
                frame = []
            else:
                frame.append(line)


if __name__ == '__main__':
    h = Hangover()
    while not h.game_over:
        print(h.draw_a_part())

