class Table:
    def __init__(self, places_numb):
        self.table_state = {k: ' ' for k in range(places_numb)}

    def put_a_char(self, char, where):
        self.table_state[where] = char

    def display(self):
        score = ' '.join(self.table_state.values())
        under = ' '.join('_'*len(self.table_state))
        return score  + '\n' + under

if __name__ == '__main__':
    tb = Table(7)
    tb.put_a_char('a', 3)
    print(tb.display())
