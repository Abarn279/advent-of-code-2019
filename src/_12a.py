from file_importer import FileImporter
import re
from aoc_utils import Vector3
from itertools import combinations

class Moon:
    def __init__(self, pos: Vector3):
        self.pos = pos
        self.vel = Vector3()
    def __repr__(self):
        return str.format("Position: {0} / Velocity: {1}", self.pos, self.vel)
    def apply_gravity(self, other):
        for component in ['x', 'y', 'z']:
            if getattr(self.pos, component) < getattr(other.pos, component):
                setattr(self.vel, component, getattr(self.vel, component) + 1)
            elif getattr(self.pos, component) > getattr(other.pos, component):
                setattr(self.vel, component, getattr(self.vel, component) - 1)
    def update(self):
        self.pos.x += self.vel.x; self.pos.y += self.vel.y; self.pos.z += self.vel.z
    def potential_energy(self):
        return abs(self.pos.x) + abs(self.pos.y) + abs(self.pos.z)
    def kinetic_energy(self):
        return abs(self.vel.x) + abs(self.vel.y) + abs(self.vel.z)
    def total_energy(self):
        return self.kinetic_energy() * self.potential_energy()

inp = FileImporter.get_input("/../input/12.txt").split("\n")

moons = [Moon(Vector3(*map(int, re.match('<x=(-?\d+),\s*y=(-?\d+),\s*z=(-?\d+)>', i).groups()))) for i in inp]
steps = 1000

for step in range(steps):
    for combo in combinations(moons, 2):
        combo[0].apply_gravity(combo[1])
        combo[1].apply_gravity(combo[0])
    
    for moon in moons:
        moon.update()
    
print(sum(moon.total_energy() for moon in moons))