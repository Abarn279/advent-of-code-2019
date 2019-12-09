from file_importer import FileImporter
from intcode_computer import IntcodeComputer

prog = list(map(int, FileImporter.get_input("/../input/9.txt").split(",")))

computer = IntcodeComputer(prog, [1])

while not computer.halted:
    print(computer.get_output())