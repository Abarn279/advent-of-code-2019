from file_importer import FileImporter
from intcode_computer import IntcodeComputer
from aoc_utils import Vector2
from collections import defaultdict

class KeyDefaultDict(dict):
    def __init__(self, factory):
        self.factory = factory
    def __missing__(self, key):
        self[key] = self.factory(key)
        return self[key]

def get_limits(grid):
    return {
        "y": (min(i.y for i in grid.keys()), max(i.y for i in grid.keys())),
        "x": (min(i.x for i in grid.keys()), max(i.x for i in grid.keys()))
    }

def print_grid(grid, pos):
    limits = get_limits(grid)
    for y in range(0, limits["y"][1] + 1):
        for x in range(0, limits["x"][1] + 1):
            ch = '#' if grid[Vector2(x, y)] == 1 else '.'
            if Vector2(x, y) == pos:
                ch = '█'
            print(ch, end="")
        print()

def get_point(pos: Vector2): 
    ''' Default factory for default dict implementation '''
    computer = IntcodeComputer(prog)
    computer.inputs = [pos.x, pos.y]
    return computer.get_output()

def check_grid_square(grid, pos, size):
    if pos.x == 35 and pos.y == 20:
        print()
    for y in range(pos.y, pos.y + size):
        for x in reversed(range(pos.x - size, pos.x)):
            if grid[Vector2(x, y)] == 0:
                return False
    return True


prog = list(map(int, FileImporter.get_input("/../input/19.txt").split(",")))
grid = KeyDefaultDict(get_point)

def find_first_square(grid):
    for x in range(0, 1000000):
        if x < 3: continue
        for y in range(0, 1000000): 
            if x == 35 and y == 20:
                print()
            if grid[Vector2(x, y)] == 1:
                c_pos = Vector2(x, y)
                while True:
                    n_pos = c_pos + Vector2(1, 0)
                    if grid[n_pos] == 1: 
                        c_pos = n_pos
                    else:
                        break

                if check_grid_square(grid, c_pos, 10):
                    print_grid(grid, c_pos)
                    return Vector2(c_pos.x - 10, c_pos.y)
                else:
                    break

pos = find_first_square(grid)
print(pos)
