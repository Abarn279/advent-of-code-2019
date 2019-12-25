from file_importer import FileImporter
from collections import deque, defaultdict
from aoc_utils import Vector2
import string
from sys import maxsize as MAXSIZE
from searches import astar

class Node(Vector2):
    def __init__(self, x, y):
        super().__init__(x, y)
    def __add__(self, other):
        return Node(self.x + other.x, self.y + other.y)
    def __lt__(self, other):
        return False
    def __repr__(self):
        return "Node: " + super().__repr__()
    def __str__(self):
        return self.__repr__()

DIRECTIONS = [Node(0, 1), Node(0, -1), Node(1, 0), Node(-1, 0)]
IMPASSABLES = set(string.ascii_uppercase + '#')

def get_limits(grid):
    return {
        "y": (min(i.y for i in grid.keys()), max(i.y for i in grid.keys())),
        "x": (min(i.x for i in grid.keys()), max(i.x for i in grid.keys()))
    }

def print_grid(grid, cl):
    limits = get_limits(grid)
    for y in range(limits["y"][0], limits["y"][1] + 1):
        for x in range(limits["x"][0], limits["x"][1] + 1):
            print('@' if cl == Node(x, y) else grid[Node(x, y)], end="")
        print()


def get_available_keys(grid, current_location, not_including = ""):
    ''' A* to find available keys '''

    global DIRECTIONS
    global IMPASSABLES

    all_keys = list([i for i in grid.items() if i[1] in set(string.ascii_lowercase) -set(not_including)])
    available_keys = []
    for location, _id in all_keys:

        visited = set()

        def is_goal_fn(location):
            x = grid[location]
            return x == _id

        def heuristic(l): 
            return l.manhattan_distance(location)

        def cost(a, b):
            return 1

        def get_neighbors(l):
            neighbors = []
            for d in DIRECTIONS:
                neighbor = l + d

                if neighbor in visited:
                    continue

                if grid[neighbor] in IMPASSABLES:
                    continue
                visited.add(neighbor)

                neighbors.append(neighbor)

            return neighbors
                
        def get_key_fn(l):
            return str(l)

        d = astar(current_location, is_goal_fn, heuristic, cost, get_neighbors, get_key_fn)
        if d is not None:
            available_keys.append((location, d))

    return available_keys
    
def get_shortest_path(grid, starting_position):
    ''' Get shortest path to getting all keys '''

    ####
    # A* NODE IS TUPLE -> (string of current keys, current cost, current grid, current location)
    # Indexed by:         (0                     , 1           , 2           , 3               )
    ####
    num_keys = sum(1 for i in grid.values() if i in string.ascii_lowercase)

    def is_goal_fn(node):
        return len(node[0]) == num_keys

    def heuristic(node): 
        return num_keys - len(node[0])

    def cost(a, b):
        return b[1] - a[1] 

    def get_neighbors(node):
        keys = get_available_keys(node[2], node[3], node[0])
        neighbors = []

        for key_point, distance_to in keys:

            # Clone grid, grab position of key, recurse after deleting that key
            new_grid = node[2].copy()
            new_position = key_point

            # Chars for key and door
            key_char = new_grid[new_position]
            door_char = str.upper(key_char)

            # Delete key and door
            door_locations = [i for i in new_grid.keys() if new_grid[i] == door_char]
            if len(door_locations) == 1:
                new_grid[door_locations[0]] = '.'
            new_grid[new_position] = '.'

            new_node = (node[0] + key_char, node[1] + distance_to, new_grid, key_point)
            neighbors.append(new_node)
        return neighbors
            
    def get_key_fn(node):
        return node[0]

    return astar(("", 0, grid, starting_position), is_goal_fn, heuristic, cost, get_neighbors, get_key_fn)

# Input and stuff
grid = {}
inp = FileImporter.get_input("/../input/18.txt").split("\n")
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid[Node(x, y)] = inp[y][x]

[starting_position] = [i for i in grid.items() if i[1] == '@']
grid[starting_position[0]] = '.'

print(get_shortest_path(grid, starting_position[0]))
