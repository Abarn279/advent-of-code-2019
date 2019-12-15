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

def print_grid(grid, current_pos):
    limits = get_limits(grid)
    for y in reversed(range(limits["y"][0], limits["y"][1] + 1)):
        for x in range(limits["x"][0], limits["x"][1] + 1):
            print('D' if current_pos == Vector2(x, y) else grid[Vector2(x, y)], end="")
        print()
    print()


DIRECTIONS = {1: Vector2(0, 1), 2: Vector2(0, -1), 3: Vector2(-1, 0), 4: Vector2(1, 0)}

prog = list(map(int, FileImporter.get_input("/../input/15.txt").split(",")))
computer = IntcodeComputer(prog)

grid = defaultdict(lambda: ' ')
grid[Vector2(0, 0)] = '.'

current_pos = Vector2(0, 0)

while True:
    possible_moves = deque()

    # Get possible moves
    m = [1, 2, 3, 4]
    shuffle(m) 
    for pd in m:
        new_pos = current_pos + DIRECTIONS[pd]
        
        if grid[new_pos] == '#':
            continue
        elif grid[new_pos] == '.':
            possible_moves.append(pd)
        else:
            possible_moves.appendleft(pd)

    # Set input as first move in possible_moves
    computer.inputs = [possible_moves[0]]
    out = computer.get_output()

    if out == 0:
        grid[current_pos + DIRECTIONS[possible_moves[0]]] = '#'

    elif out == 1:
        current_pos = current_pos + DIRECTIONS[possible_moves[0]]
        grid[current_pos] = '.'
    
    elif out == 2:
        current_pos = current_pos + DIRECTIONS[possible_moves[0]]
        grid[current_pos] = 'O'
        break

def do_bfs():
    global grid

    q = deque()
    visited = set()
    q.append((Vector2(0, 0), 0)) # Tuple of position to distance from start

    while len(q) > 0:
        c = q.popleft()
        visited.add(c[0])

        for surrounding in [c[0] + i for i in DIRECTIONS.values()]:
            if grid[surrounding] == 'O':
                return c[1] + 1

            if grid[surrounding] not in ['#', ' '] and surrounding not in visited:
                q.append((surrounding, c[1] + 1))

print(do_bfs())
