from file_importer import FileImporter
from collections import deque, defaultdict
from aoc_utils import Vector2
import string

DIRECTIONS = [Vector2(0, 1), Vector2(0, -1), Vector2(1, 0), Vector2(-1, 0)]

def get_limits(grid):
    return {
        "y": (min(i.y for i in grid.keys()), max(i.y for i in grid.keys())),
        "x": (min(i.x for i in grid.keys()), max(i.x for i in grid.keys()))
    }

def print_grid(grid, cl):
    limits = get_limits(grid)
    for y in range(limits["y"][0], limits["y"][1] + 1):
        for x in range(limits["x"][0], limits["x"][1] + 1):
            print('█' if cl == Vector2(x, y) else grid[Vector2(x, y)], end="")
        print()

def get_portal_name(grid, pos):
    if grid[pos + Vector2(0, -1)] in string.ascii_uppercase: # TOP
        return grid[pos + Vector2(0, -1)] + grid[pos]
    elif grid[pos + Vector2(-1, 0)] in string.ascii_uppercase: # LEFT
        return grid[pos + Vector2(-1, 0)] + grid[pos] 
    elif grid[pos + Vector2(1, 0)] in string.ascii_uppercase: # RIGHT
        return grid[pos] + grid[pos + Vector2(1, 0)]
    elif grid[pos + Vector2(0, 1)] in string.ascii_uppercase: # BOTTOM
        return grid[pos] + grid[pos + Vector2(0, 1)]
    raise Exception()
   
def find_portals(grid):
    limits = get_limits(grid)
    
    portal_entrances = defaultdict(list)

    for y in range(limits["y"][0], limits["y"][1] + 1):
        for x in range(limits["x"][0], limits["x"][1] + 1):
            if grid[Vector2(x, y)] in string.ascii_uppercase:
                if grid[Vector2(x, y + 1)] in string.ascii_uppercase and grid[Vector2(x, y + 2)] == '.':  # TOP
                    portal_entrances[grid[Vector2(x, y)] + grid[Vector2(x, y + 1)]].append(Vector2(x, y + 2))
                elif grid[Vector2(x + 1, y)] in string.ascii_uppercase and grid[Vector2(x + 2, y)] == '.':  # LEFT
                    portal_entrances[grid[Vector2(x, y)] + grid[Vector2(x + 1, y)]].append(Vector2(x + 2, y))
                elif grid[Vector2(x + 1, y)] in string.ascii_uppercase and grid[Vector2(x - 1, y)] == '.':  # RIGHT
                    portal_entrances[grid[Vector2(x, y)] + grid[Vector2(x + 1, y)]].append(Vector2(x - 1, y))
                if grid[Vector2(x, y + 1)] in string.ascii_uppercase and grid[Vector2(x, y - 1)] == '.':  # BOTTOM
                    portal_entrances[grid[Vector2(x, y)] + grid[Vector2(x, y + 1)]].append(Vector2(x, y - 1))
    return portal_entrances

def get_distance(grid, start_pos, end_pos, portal_entrances):
    global DIRECTIONS

    valid_moves = string.ascii_uppercase + '.'

    q = deque()
    visited = set()
    q.append((start_pos, 0))  

    while len(q) > 0:
        p, d = q.popleft()

        visited.add(p)

        if p == end_pos:
            return d

        for direction in DIRECTIONS:
            n_p = p + direction
            n_d = d + 1

            if n_p not in visited and grid[n_p] in valid_moves:
                
                if grid[n_p] in string.ascii_uppercase:                 # If portal
                    portal_name = get_portal_name(grid, n_p)
                    if portal_name in ['AA', 'ZZ']:
                        continue
                    [other_pos] = [i for i in portal_entrances[portal_name] if i != p]
                    n_p = other_pos
                
                q.append((n_p, n_d))

# Input and stuff
grid = defaultdict(lambda: ' ') 
inp = FileImporter.get_input("/../input/20.txt").split("\n")
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid[Vector2(x, y)] = inp[y][x]

portal_entrances = find_portals(grid)

start_pos = portal_entrances['AA'][0]
end_pos = portal_entrances['ZZ'][0]

print(get_distance(grid, start_pos, end_pos, portal_entrances))