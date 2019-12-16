from file_importer import FileImporter
from intcode_computer import IntcodeComputer
from aoc_utils import Vector2
from collections import deque, defaultdict
from random import shuffle

def get_limits(grid):
    return {
        "y": (min(i.y for i in grid.keys()), max(i.y for i in grid.keys())),
        "x": (min(i.x for i in grid.keys()), max(i.x for i in grid.keys()))
    }

def print_grid(grid):
    limits = get_limits(grid)
    for y in reversed(range(limits["y"][0], limits["y"][1] + 1)):
        for x in range(limits["x"][0], limits["x"][1] + 1):
            print('█' if grid[Vector2(x, y)] == ' ' else grid[Vector2(x, y)], end="")
        print()
    print()


DIRECTIONS = {1: Vector2(0, 1), 2: Vector2(0, -1), 3: Vector2(-1, 0), 4: Vector2(1, 0)}

prog = list(map(int, FileImporter.get_input("/../input/15.txt").split(",")))
computer = IntcodeComputer(prog)

grid = defaultdict(lambda: ' ')
grid[Vector2(0, 0)] = '.'

current_pos = Vector2(0, 0)
visited = set([Vector2(0, 0)])
q = deque()
for i in [1, 2, 3, 4]:
    q.append((current_pos, i, computer.clone()))

while len(q) > 0:

    # Grab the queued old position, direction, computer, and make the move to the new position with that info
    c_position, direction, comp = q.popleft()

    # This will be the new position on the grid
    n_position = c_position + DIRECTIONS[direction]
    visited.add(n_position)

    # Run computer, set grid based on output
    comp.inputs = [direction]
    out = comp.get_output()

    # If wall, continue loop as we dont want to keep searching
    if out == 0:
        grid[n_position] = '#'
        continue

    elif out == 1:
        grid[n_position] = '.'
    
    elif out == 2:
        grid[n_position] = 'O'

    for direction in [1, 2, 3, 4]:
        if n_position + DIRECTIONS[direction] not in visited: 
            q.append((n_position, direction, comp.clone()))

print_grid(grid)
