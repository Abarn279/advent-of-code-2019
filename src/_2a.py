from file_importer import FileImporter
import math

inp = list(map(int, FileImporter.get_input("/../input/2.txt").split(",")))
inp[1] = 12
inp[2] = 2

for i in range(0, len(inp), 4):
    if inp[i] == 99: break
    inp[inp[i+3]] = inp[inp[i+1]] + inp[inp[i+2]] if inp[i] == 1 else inp[inp[i+1]] * inp[inp[i+2]]

print(inp[0])
