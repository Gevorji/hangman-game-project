class Hangman:
    def __init__(self, max_failures, animation_frames):
        self.max_failures = max_failures
        self.animation_frames = animation_frames
        self.alive_parts_counter = self.max_failures
        self.its_gameover = False

    def add_one_part(self):
        if not self.its_gameover:
            self.alive_parts_counter -= 1
        if self.alive_parts_counter == 0:
            self.its_gameover = True

    def display(self):
        frame_idx = 0 if self.max_failures == self.alive_parts_counter else self.max_failures-self.alive_parts_counter
        return self.animation_frames[frame_idx]



if __name__ == '__main__':
    frames = open('body_art.txt', encoding='utf-8')
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
    h = Hangman(6, process_frames(frames))
    print(h.display())
    while not h.its_gameover:
        h.add_one_part()
        print('One step closer to be hanged')
        print(h.display())

