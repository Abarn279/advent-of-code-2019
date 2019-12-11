from file_importer import FileImporter
from intcode_computer import IntcodeComputer
from collections import defaultdict
from aoc_utils import Vector2

DIRECTIONS = {0: Vector2(0, 1), 1: Vector2(1, 0), 2: Vector2(0, -1), 3: Vector2(-1, 0)}

prog = list(map(int, FileImporter.get_input("/../input/11.txt").split(",")))

computer = IntcodeComputer(prog)
grid = defaultdict(lambda: '.')
direction = 0
position = Vector2(0, 0)

painted_once = set()

while not computer.halted:

    inp = 0 if grid[position] == '.' else 1
    computer.inputs.append(inp)

    paint_output = computer.get_output()
    grid[position] = '.' if paint_output == 0 else 1
    painted_once.add(position)

    turn_output = computer.get_output()
    if turn_output == 0:
        direction -= 1
    else:
        direction += 1
    direction = direction % 4

    position = position + DIRECTIONS[direction]

print(len(painted_once))