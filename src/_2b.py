from file_importer import FileImporter
import math

inp = list(map(int, FileImporter.get_input("/../input/2.txt").split(",")))

def mul_noun_verb(prog):
    for noun in range(100):
        for verb in range(100):
            inp = prog[:]
            inp[1] = noun; inp[2] = verb
            for i in range(0, len(inp), 4):
                if inp[i] == 99: break
                inp[inp[i+3]] = inp[inp[i+1]] + inp[inp[i+2]] if inp[i] == 1 else inp[inp[i+1]] * inp[inp[i+2]]
            if inp[0] == 19690720:
                return 100 * noun + verb

print(mul_noun_verb(inp))
