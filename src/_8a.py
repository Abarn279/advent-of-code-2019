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

num_zeroes_per_layer = []
for i in layers:
    num_zeroes_per_layer.append(sum(1 for v in i.values() if v == 0))
least_zero_layer = layers[num_zeroes_per_layer.index(min(num_zeroes_per_layer))]

print(sum(1 for i in least_zero_layer.values() if i == 1) * sum(1 for i in least_zero_layer.values() if i == 2))
        