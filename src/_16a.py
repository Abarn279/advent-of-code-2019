from file_importer import FileImporter
from collections import deque
from itertools import cycle

def do_fft(numbers):
    output = ""
    for i in range(len(numbers)): 

        pattern = [0] * (i + 1) + [1] * (i + 1) + [0] * (i + 1) + [-1] * (i + 1)  # Not sure if a great optimization but didn't want to pop(0) off front of list continuously
        pattern_cycle = cycle(pattern)
        next(pattern_cycle)

        digit = 0
        for n in numbers:
            digit += int(n) * next(pattern_cycle)

        output = output + str(abs(digit) % 10)
    return output

        

inp = FileImporter.get_input("/../input/16.txt")

for i in range(100): 
    inp = do_fft(inp)

print(inp[:8])