from file_importer import FileImporter
from aoc_utils import Vector2
import math

inp = FileImporter.get_input("/../input/10.txt").split("\n")

grid = {}
for y in range(len(inp)):
    for x in range(len(inp[y])):
        grid[Vector2(x, y)] = inp[y][x]

asteroids = [v for v, c in grid.items() if c == '#']

max_seen = 0
coords = None
for asteroid in asteroids:
    angles_seen = [] # List of ratios of opposite to adjacent sides of triangles (in place of angles)
                     # that are already seen, so that we cannot see any behind them

    others = [a for a in asteroids if a != asteroid]
    others = list(sorted(others, key = lambda x: x.manhattan_distance(asteroid)))

    num_seen = 0
    for other_a in others: 
        angle =  math.atan2(other_a.y - asteroid.y, other_a.x - asteroid.x)

        if angle in angles_seen: # Can't see this asteroid because it's behind another
            continue

        angles_seen.append(angle)
        num_seen += 1
    if num_seen > max_seen:
        max_seen = num_seen
        coords = asteroid

print(max_seen)
print(coords)