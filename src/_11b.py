from file_importer import FileImporter
from intcode_computer import IntcodeComputer
from collections import defaultdict
from aoc_utils import Vector2

def get_limits(grid):
    return {
        "y": (min(i.y for i in grid.keys()), max(i.y for i in grid.keys())),
        "x": (min(i.x for i in grid.keys()), max(i.x for i in grid.keys()))
    }

def print_grid(grid):
    limits = get_limits(grid)
    for y in reversed(range(limits["y"][0], limits["y"][1] + 1)):
        for x in range(limits["x"][0], limits["x"][1] + 1):
            print('█' if grid[Vector2(x, y)] == '#' else ' ', end="")
        print()

DIRECTIONS = {0: Vector2(0, 1), 1: Vector2(1, 0), 2: Vector2(0, -1), 3: Vector2(-1, 0)}

prog = list(map(int, FileImporter.get_input("/../input/11.txt").split(",")))

computer = IntcodeComputer(prog)
grid = defaultdict(lambda: '.')
grid[Vector2(0,0)] = '#'
direction = 0
position = Vector2(0, 0)

painted_once = set()

while not computer.halted:

    inp = 0 if grid[position] == '.' else 1
    computer.inputs.append(inp)

    paint_output = computer.get_output()
    grid[position] = '.' if paint_output == 0 else '#'
    painted_once.add(position)

    turn_output = computer.get_output()
    if turn_output == 0:
        direction -= 1
    else:
        direction += 1
    direction = direction % 4

    position = position + DIRECTIONS[direction]

print_grid(grid)