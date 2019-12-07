from file_importer import FileImporter
from itertools import permutations
from intcode_computer import IntcodeComputer

prog = list(map(int, FileImporter.get_input("/../input/7.txt").split(",")))

ps_permutations = [list(map(int, i)) for i in list(permutations("01234"))]
max_output = -1
for ps_perm in ps_permutations:

    # This will be the output of each amp, starting at 0 for the first one
    output = 0                                                          

    for phase_setting in ps_perm:
        comp = IntcodeComputer(prog[:], [phase_setting, output])
        output = comp.get_output()
    
    if output > max_output: max_output = output

print(max_output)