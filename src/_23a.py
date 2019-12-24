from file_importer import FileImporter
from intcode_computer import IntcodeComputer

prog = list(map(int, FileImporter.get_input("/../input/23.txt").split(",")))
computers = {i: IntcodeComputer(prog, [i]) for i in range(50)}

def get_255(computers):
    while True: 
        for computer in computers.values():
            if len(computer.inputs) <= 1:      # 1 to account for initial address input
                computer.inputs.append(-1)

            a, x, y = [computer.get_output() for i in range(3)]

            if any(True for i in [a, x, y] if i == None):
                continue

            if a == 255:
                return y

            computers[a].inputs += [x, y]

print(get_255(computers))