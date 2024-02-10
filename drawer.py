class Drawer:
    def __init__(self, frames_file):
        self.frames = self.process_frames(frames_file)
        self.frame_counter = 0

    def process_frames(self, file):
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

    def draw_a_frame(self):
        if self.frame_counter > len(self.frames)-1:
            self.frame_counter = 0
            print(self.frames[self.frame_counter])
        else:
            print(self.frames[self.frame_counter])
            self.frame_counter += 1

    def draw_a_frozen_frame(self):
        frame_idx = self.frame_counter if self.frame_counter == 0 else self.frame_counter - 1
        print(self.frames[frame_idx])


if __name__ == '__main__':
    frames_file = open('body_art.txt', encoding='utf-8')
    drawer = Drawer(frames_file=frames_file)
    import os, time
    for i in range(6):
        drawer.draw_a_frame()
        time.sleep(1)
        os.system('cls')

