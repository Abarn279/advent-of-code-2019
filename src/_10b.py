from file_importer import FileImporter
from aoc_utils import Vector2
import math
from collections import defaultdict, deque

inp = FileImporter.get_input("/../input/10.txt").split("\n")

grid = {}
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid[Vector2(x, y)] = inp[y][x]

station = Vector2(30, 34) # FROM PART A
asteroids = [v for v, c in grid.items() if c == '#' and v != station]

# Build a dictionary of angles from the station to the asteroids that are in line with those angles
asteroids_by_angle = defaultdict(list)
for asteroid in asteroids:
    angle = math.atan2(station.y - asteroid.y, station.x - asteroid.x)
    asteroids_by_angle[angle].append(asteroid)

# Sort each list of angles to asteroids by manhattan distance from station
for k in asteroids_by_angle.keys():
    asteroids_by_angle[k] = list(sorted(asteroids_by_angle[k], key = lambda x: x.manhattan_distance(station)))

# Create a deque of the angles and rotate until we're pointing up
sorted_asteroids = deque(sorted(asteroids_by_angle.items(), key=lambda x: x[0]))
while sorted_asteroids[0][0] < math.pi / 2:
    sorted_asteroids.rotate(-1)

# Rotate and blast
blasts = 0
_200th = None
while True:
    if len(sorted_asteroids[0][1]) > 0:
        blasts += 1
        if blasts == 200:
            _200th = sorted_asteroids[0][1].pop(0)
            break
        sorted_asteroids[0][1].pop(0)

    sorted_asteroids.rotate(-1)

print(_200th.x * 100 + _200th.y)
