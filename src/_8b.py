from file_importer import FileImporter
from collections import defaultdict, deque

# Reversed so we can pop from 
data = deque(map(int, FileImporter.get_input("/../input/8.txt")))

# From prompt
w = 25
h = 6
px_per_layer = w * h
n_layers = len(data) // px_per_layer
layers = [None for i in range(n_layers)]

for l in range(n_layers):
    layer = defaultdict(lambda: None)
    for y in reversed(range(h)):
        for x in range(w):
            layer[(x, y)] = data.popleft()
    layers[l] = layer

final = defaultdict(lambda: 2)

# Set top pixels in reverse order
for layer in reversed(layers):
    for key in layer.keys():
        if layer[key] != 2:
            final[key] = layer[key]

# Draw in command prompt
for y in reversed(range(h)):
    for x in range(w):
        print('█' if final[(x, y)] != 0 else " " , end="")  # Lol ascii
    print()