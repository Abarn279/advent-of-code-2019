from file_importer import FileImporter
from intcode_computer import IntcodeComputer
from aoc_utils import Vector2
from collections import defaultdict

DIRECTIONS = [Vector2(0, 1), Vector2(0, -1), Vector2(1, 0), Vector2(-1, 0)]

def get_limits(grid):
    return {
        "y": (min(i.y for i in grid.keys()), max(i.y for i in grid.keys())),
        "x": (min(i.x for i in grid.keys()), max(i.x for i in grid.keys()))
    }

def print_grid(grid):
    limits = get_limits(grid)
    for y in range(limits["y"][0], limits["y"][1] + 1):
        for x in range(limits["x"][0], limits["x"][1] + 1):
            print(grid[Vector2(x, y)], end="")
        print()
    print()

def get_input_line(st):
    l = list(map(ord, list(st)))
    if len(l) > 20:
        raise Exception("20 chars!")
    return l + [10]

prog = list(map(int, FileImporter.get_input("/../input/17.txt").split(",")))

computer = IntcodeComputer(prog)
computer.prog[0] = 2

computer.inputs += get_input_line('A,B,A,B,C,C,B,A,C,A')
computer.inputs += get_input_line('L,10,R,8,R,6,R,10')
computer.inputs += get_input_line('L,12,R,8,L,12')
computer.inputs += get_input_line('L,10,R,8,R,8')
computer.inputs += get_input_line('n')

img = defaultdict(lambda: ' ')

y = 0
x = 0

# Set img
while not computer.halted:
    c = computer.get_output()
    if c > 1000:
        print(c)
        break
    if c == None:
        break
    elif c == 10:
        y += 1
        x = 0
        continue
    img[Vector2(x, y)] = chr(c)     # Convert from ascii
    x += 1

initial_bot = [i for i in img.keys() if img[i] == '^']

print_grid(img)
