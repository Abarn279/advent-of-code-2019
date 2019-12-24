from file_importer import FileImporter
from collections import defaultdict
from aoc_utils import Vector2
import numpy

DIRECTIONS = [Vector2(0, 1), Vector2(0, -1), Vector2(1, 0), Vector2(-1, 0)]

n_adjacent = lambda grid, pos: sum(1 for d in DIRECTIONS if grid[pos + d] == '#')

get_biod_r = lambda st: sum(2 ** idx for idx, item in enumerate(st) if item == '#')

get_hashable = lambda grid: "".join([grid[Vector2(x, y)] for y in range(5) for x in range(5)])

# Input 
inp = FileImporter.get_input("/../input/24.txt").split("\n")
grid = defaultdict(lambda: ' ')
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid[Vector2(x, y)] = inp[y][x]

# Algo
layouts = set()
layouts.add(get_hashable(grid))
while True:
    n_grid = grid.copy()
    keys = list(grid.keys())
    for key in keys:
        if grid[key] == '#' and n_adjacent(grid, key) != 1:
            n_grid[key] = '.'
        elif grid[key] == '.' and n_adjacent(grid, key) in [1, 2]:
            n_grid[key] = '#'
    grid = n_grid

    # lol
    g_string = get_hashable(grid)
    if g_string in layouts:
        print(get_biod_r(g_string))
        break
    layouts.add(g_string) 