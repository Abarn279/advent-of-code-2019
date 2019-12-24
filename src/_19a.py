from file_importer import FileImporter
from intcode_computer import IntcodeComputer
from aoc_utils import Vector2

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

prog = list(map(int, FileImporter.get_input("/../input/19.txt").split(",")))
grid = {}

for y in range(50):
    for x in range(50): 
        computer = IntcodeComputer(prog)
        computer.inputs = [x, y]
        output = computer.get_output()
        grid[Vector2(x, y)] = output

print(sum(1 for i in grid.values() if i == 1))