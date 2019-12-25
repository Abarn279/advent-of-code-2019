from file_importer import FileImporter
from intcode_computer import IntcodeComputer

def get_output_str(computer):
    st = ""
    while True:
        out = computer.get_output()
        if out is not None :
            st += chr(out)
        else:
            break
    return st

get_ascii = lambda st: list(map(ord, list(st))) + [10]
prog = list(map(int, FileImporter.get_input("/../input/25.txt").split(",")))
computer = IntcodeComputer(prog)

commands = [
    "east"
]

print(get_output_str(computer))

for c in commands:
    computer.inputs += get_ascii(c)
    print(get_output_str(computer))
    
    
    