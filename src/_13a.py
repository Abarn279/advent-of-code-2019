from file_importer import FileImporter
from intcode_computer import IntcodeComputer

class Tile:
    def __init__(self, x, y, id):
        self.x = x 
        self.y = y
        self.id = id

prog = list(map(int, FileImporter.get_input("/../input/13.txt").split(",")))

computer = IntcodeComputer(prog)

tiles = []
while not computer.halted:
    tiles.append(Tile(*[computer.get_output() for _ in range(3)]))

print(len([i for i in tiles if i.id == 2]))