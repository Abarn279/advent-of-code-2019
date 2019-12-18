from file_importer import FileImporter
from intcode_computer import IntcodeComputer
from aoc_utils import Vector2

DIRECTIONS = [Vector2(0, 1), Vector2(0, -1), Vector2(1, 0), Vector2(-1, 0)]

def get_limits(grid):
    return {
        "y": (min(i.y for i in grid.keys()), max(i.y for i in grid.keys())),
        "x": (min(i.x for i in grid.keys()), max(i.x for i in grid.keys()))
    }

def print_grid(grid):
    limits = get_limits(grid)
    for y in reversed(range(limits["y"][0], limits["y"][1] + 1)):
        for x in range(limits["x"][0], limits["x"][1] + 1):
            print(grid[Vector2(x, y)], end="")
        print()
    print()

prog = list(map(int, FileImporter.get_input("/../input/17.txt").split(",")))
computer = IntcodeComputer(prog)
img = {}

y = 0
x = 0

# Set img
while not computer.halted:
    c = computer.get_output()
    if c == None:
        break
    elif c == 10:
        y += 1
        x = 0
        continue
    img[Vector2(x, y)] = chr(c)     # Convert from ascii
    x += 1

def surrounded_by_scaffold(grid, point):
    global DIRECTIONS
    return all(point + i in grid and grid[point + i] == '#' for i in DIRECTIONS)

all_scaffold_points = [i for i in img.keys() if img[i] == '#' and surrounded_by_scaffold(img, i)]

print(sum(i.x * i.y for i in all_scaffold_points))
print_grid(img)