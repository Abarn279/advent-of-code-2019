from file_importer import FileImporter
import re
from aoc_utils import Vector3
from itertools import combinations
from math import gcd
from functools import reduce

# https://gist.github.com/endolith/114336
def lcm(*numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return reduce(lcm, numbers, 1)

class Moon:
    def __init__(self, pos: Vector3):
        self.pos = pos
        self.vel = Vector3()
        self.repeatx = None
        self.repeaty = None
        self.repeatz = None

    def __repr__(self):
        return str.format("(Position: {0} / Velocity: {1}", self.pos, self.vel) + str.format(" // REPEATS: x: {0}, y: {1}, z: {2})", self.repeatx, self.repeaty, self.repeatz)
    def __str__(self): 
        return self.__repr__()
    def __eq__(self, other):
        return self.pos == other.pos and self.vel == other.vel
    def clone(self):
        return Moon(self.pos.clone())
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

def all_set(moons):
    for i in moons:
        for c in ["x", "y", "z"]:
            if getattr(i, "repeat" + c) == None:
                return False
    return True

inp = FileImporter.get_input("/../input/12.txt").split("\n")

moons = [Moon(Vector3(*map(int, re.match('<x=(-?\d+),\s*y=(-?\d+),\s*z=(-?\d+)>', i).groups()))) for i in inp]
initials = [i.clone() for i in moons]
steps = 100000000

lcms = []

for step in range(steps):
    for moon_i in range(len(moons)):
        for c in ["x", "y", "z"]:
            if getattr(moons[moon_i].pos, c) == getattr(initials[moon_i].pos, c) and getattr(moons[moon_i].vel, c) == 0 and getattr(moons[moon_i], "repeat" + c) is None and step != 0:
                setattr(moons[moon_i], "repeat" + c, step)

    if all_set(moons):
        components = [i.repeatx for i in moons] + [i.repeaty for i in moons] + [i.repeatz for i in moons]
        print(lcm(*components))
        break

    for combo in combinations(moons, 2):
        combo[0].apply_gravity(combo[1])
        combo[1].apply_gravity(combo[0])
    
    for moon in moons:
        moon.update()