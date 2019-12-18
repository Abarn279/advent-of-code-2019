from file_importer import FileImporter
from intcode_computer import IntcodeComputer
from aoc_utils import Vector2
from collections import defaultdict

def get_input_line(st):
    return list(map(ord, list(st))) + [10]

prog = list(map(int, FileImporter.get_input("/../input/17.txt").split(",")))

computer = IntcodeComputer(prog)
computer.prog[0] = 2

computer.inputs += get_input_line('A,B,A,B,C,C,B,A,C,A')
computer.inputs += get_input_line('L,10,R,8,R,6,R,10')
computer.inputs += get_input_line('L,12,R,8,L,12')
computer.inputs += get_input_line('L,10,R,8,R,8')
computer.inputs += get_input_line('n')

img = defaultdict(lambda: ' ')

y = 0
x = 0

while not computer.halted:
    c = computer.get_output()
    if c > 1000:
        print(c)
        break
    if c == None:
        break
    elif c == 10:
        y += 1
        x = 0
        continue
    img[Vector2(x, y)] = chr(c)     # Convert from ascii
    x += 1
