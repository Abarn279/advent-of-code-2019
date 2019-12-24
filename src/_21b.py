from file_importer import FileImporter
from intcode_computer import IntcodeComputer

def get_input(st):
    return list(map(ord, list(st))) + [10]

prog = list(map(int, FileImporter.get_input("/../input/21.txt").split(",")))
code = """\
OR A J
NOT B T
AND T J
NOT C T
AND T J
AND D J
NOT A T
OR T J
NOT C T
AND A T
AND B T
AND D T
OR T J
RUN"""

computer = IntcodeComputer(prog, get_input(code))

while not computer.halted:
    out = computer.get_output()
    if out is not None:
        if out < 0x110000:
            print(chr(out), end="")
        else: print(out)