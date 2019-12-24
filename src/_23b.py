from file_importer import FileImporter
from intcode_computer import IntcodeComputer

prog = list(map(int, FileImporter.get_input("/../input/23.txt").split(",")))
computers = {i: IntcodeComputer(prog, [i]) for i in range(50)}


def get_255(computers):
    nat_x_y = None
    y_vals = set()
    while True: 
        x = [len(i.inputs) == 0 for i in computers.values()]
        if all(x) and nat_x_y is not None:
            if nat_x_y[1] in y_vals:
                return nat_x_y[1]
            y_vals.add(nat_x_y[1])

            computers[0].inputs += [nat_x_y[0], nat_x_y[1]]

        for computer in computers.values():
            if len(computer.inputs) <= 1:      # 1 to account for initial address input
                computer.inputs.append(-1)

            a, x, y = [computer.get_output() for i in range(3)]

            if any(True for i in [a, x, y] if i == None):
                continue

            if a == 255:
                nat_x_y = (x, y)
                continue

            computers[a].inputs += [x, y]

print(get_255(computers))
