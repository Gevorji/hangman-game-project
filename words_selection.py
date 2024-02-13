f = open('russian_nouns.txt', encoding='utf-8')
selected = []
for line in f:
    if len(line) >= 5: selected.append(line)
import random
random.shuffle(selected)
print(selected)

import json
with open('russian_nouns_prepared.json', 'w') as dump:
    json.dump(selected, dump)
