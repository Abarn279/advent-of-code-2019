from file_importer import FileImporter
from intcode_computer import IntcodeComputer
from aoc_utils import Vector2
from collections import defaultdict
from itertools import combinations, chain

def get_output_str(computer):
    st = ""
    while True:
        out = computer.get_output()
        if out is not None :
            st += chr(out)
        else:
            break
    return st

# Setup
get_ascii = lambda st: list(map(ord, list(st))) + [10]
prog = list(map(int, FileImporter.get_input("/../input/25.txt").split(",")))
computer = IntcodeComputer(prog)

inputs = []
pre_inputs = [
"north",
"take wreath",
"south",
"east",
"take loom",
"south",
"take ornament",
"west",
"north",
"take candy cane",
"south",
"east",
"east",
"south",
"east",
"west",
"south",
"north",
"east",
"west",
"north",
"west",
"west",
"east",
"north",
"east",
"take fixed point",
"north",
"take spool of cat6",
"west",
"take shell",
"east",
"north",
"take weather machine",
"south",
"west",
"east",
"south",
"west",
"west",
"north",
"north",
"south",
"east",
"west",
"north",
"east",
"south",
"south",
"south",
"west",
"east",
"south",
"west",
"south",
"east",
"east",
"west",
"west",
"north",
"east"
]

items = [
"ornament",
"loom",
"spool of cat6",
"wreath",
"fixed point",
"shell",
"candy cane",
"weather machine"
]

item_combos = list(chain(*[list(combinations(items, i)) for i in range(1, 8)]))

# Main loop
print(get_output_str(computer))
while True:
    if len(pre_inputs) > 0:
        inp = pre_inputs.pop(0)
    else:
        inp = input("-> ")

        if inp == "g": # guess
            combo = item_combos.pop()
            for i in combo:
                pre_inputs.append("drop " + i)
            pre_inputs.append("south")
            for i in combo:
                pre_inputs.append("take " + i)
            print(combo)
            continue

        elif inp == "get": # get inputs so i can copy them and run sim up to this point next way through
            for i in inputs:
                print("\"" + i + "\",")
            continue

    inputs.append(inp)
    computer.inputs += get_ascii(inp)
    out = get_output_str(computer)
    print(out)

    print('--------------------------\n')
    
# 352325632
# drop ('ornament', 'loom', 'wreath', 'weather machine')
