from file_importer import FileImporter
from aoc_utils import Vector2
from collections import defaultdict
from uuid import uuid1

class PositionVal:
    def __init__(self, char, id, total_steps = 0):
        self.char = char; self.id = id; self.total_steps = total_steps
    def __repr__(self):
        return self.char

DIRECTIONS = {'D': Vector2(0, -1), 'R': Vector2(1, 0), 'U': Vector2(0, 1), 'L': Vector2(-1, 0)}

def draw_wire_return_crosses(grid, path):
    global DIRECTIONS
    cursor = Vector2(0,0)
    cross_points = []
    wire_id = uuid1()
    total_steps = 0

    for direction in path:

        d_v = DIRECTIONS[direction[0]]              # Direction vector
        n = int(direction[1:])                      # Number of steps to go

        for step in range(n):
            cursor = cursor + d_v
            total_steps += 1

            if grid[cursor].char != '.' and grid[cursor].id != wire_id:
                grid[cursor] = PositionVal('X', wire_id, grid[cursor].total_steps)
                cross_points.append((cursor, total_steps + grid[cursor].total_steps))
            else:
                grid[cursor] = PositionVal('|', wire_id, total_steps) if direction[0] in 'DU' else PositionVal('-', wire_id, total_steps)

        grid[cursor] = '+'

    return cross_points



inp = [i.split(',') for i in FileImporter.get_input("/../input/3.txt").split("\n")]

grid = defaultdict(lambda: PositionVal('.', None))
grid[Vector2(0, 0)] = PositionVal('o', None)

cross_points = []
for i in inp:
    cross_points = cross_points + draw_wire_return_crosses(grid, i)         # List addition

print(min(i[1] for i in cross_points))
