from file_importer import FileImporter
from itertools import permutations
from intcode_computer import IntcodeComputer

prog = list(map(int, FileImporter.get_input("/../input/7.txt").split(",")))

ps_permutations = [list(map(int, i)) for i in list(permutations("56789"))]
max_output = -1
for ps_perm in ps_permutations:

    # This will be the output of each amp, starting at 0 for the first one
    output = 0

    comps = []

    # Create computers, initial loops with phase settings
    for phase_setting in ps_perm:
        comp = IntcodeComputer(prog[:], [phase_setting, output])
        comps.append(comp)
        output = comp.get_output()

    # Feedback loop
    i = 0
    while all(not comp.halted for comp in comps):
        comps[i].inputs.append(output)
        output = comps[i].get_output()
        i = (i + 1) % len(comps)
    
    # Pull last output from amp E
    if comps[-1].last_output > max_output: max_output = comps[-1].last_output

print(max_output)