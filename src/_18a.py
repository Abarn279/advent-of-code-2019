from file_importer import FileImporter
from collections import deque, defaultdict
from aoc_utils import Vector2
import string
from sys import maxsize as MAXSIZE
from searches import astar
from time import time

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
DOORS = set(string.ascii_uppercase)

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

def get_distance_from_to_key(grid, from_key, to_key):
    ''' BFS to find distance from one key to another '''
    global DIRECTIONS
    global DOORS

    # Locations
    current_location = from_key[0]
    end_location = to_key[0]

    q = deque()
    visited = set()
    q.append((current_location, 0, [])) # BFS node is location, distance to this location, doors encountered on the way here

    while len(q) > 0:
        location, distance_to, doors_encountered = q.popleft()
        visited.add(location)

        if location == end_location:
            return (location, distance_to, doors_encountered)

        if grid[location] in DOORS:
            doors_encountered.append(grid[location])

        for direction in DIRECTIONS:
            neighbor = location + direction

            if neighbor in visited:
                continue

            if grid[neighbor] == '#':
                continue

            q.append((neighbor, distance_to + 1, doors_encountered[:]))
    
def get_shortest_path(grid, starting_position, distance_map):
    ''' Get shortest path to getting all keys '''

    ####
    # A* NODE IS TUPLE -> (string of current keys, current cost, current location)
    # Indexed by:         (0                     , 1           , 2               )
    ####
    num_keys = sum(1 for i in grid.values() if i in string.ascii_lowercase)
    min_dist = 100000
    for this_char in distance_map:
        distances = distance_map[this_char]
        for other_char_key in distances:
            other_char_pos, distance_to_other, doors_encountered = distance_map[this_char][other_char_key]
            if distance_to_other < min_dist:
                min_dist = distance_to_other

    def is_goal_fn(node):
        return len(node[0]) == num_keys

    def heuristic(node): 
        return min_dist * (num_keys - len(node[0]))

    def cost(a, b):
        return b[1] - a[1] 

    def get_neighbors(node):
        keys_acquired = set(node[0])

        this_char = grid[node[2]]
        distances_from_here = distance_map[this_char]
        keys_available = []

        # Keys are available if keys_encountered on the path is a subset of keys_acquired
        for other_char_key in distances_from_here:
            other_char_pos, distance_to_other, doors_encountered = distance_map[this_char][other_char_key]
            doors_encountered = set(map(lambda x: x.lower(), doors_encountered)) # Turn encountered keys for this path into a set

            # If all of the keys on this path have been acquired, it's a viable path
            if other_char_key[1] not in keys_acquired and doors_encountered.issubset(keys_acquired):
                keys_available.append((other_char_pos, distance_to_other, other_char_key[1]))

        neighbors = []
        for key_point, distance_to, key_char in keys_available:
            new_node = ("".join(sorted(node[0])) + key_char, node[1] + distance_to, key_point)
            neighbors.append(new_node)

        return neighbors
            
    def get_key_fn(node):
        return node[0]

    return astar(("", 0, starting_position), is_goal_fn, heuristic, cost, get_neighbors, get_key_fn)

# Input and stuff
grid = {}
inp = FileImporter.get_input("/../input/18.txt").split("\n")
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid[Node(x, y)] = inp[y][x]

# Find starting position
[starting_position] = [i for i in grid.items() if i[1] == '@']
starting_position = (starting_position[0], '.')
grid[starting_position[0]] = '.'

distance_map = defaultdict(lambda: {})       # map of key char to a map of other key chars and the distance to them 
all_keys = [i for i in grid.items() if i[1] in string.ascii_lowercase] + [starting_position]

for key in all_keys:
    other_keys = [i for i in all_keys if i[1] != key[1]]
    for other_key in other_keys:

        if other_key[1] == '.':
            continue

        distance = get_distance_from_to_key(grid, key, other_key)
        distance_map[key[1]][other_key] = distance

print(get_shortest_path(grid, starting_position[0], distance_map))
