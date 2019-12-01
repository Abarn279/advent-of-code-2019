from file_importer import FileImporter
import math

def get_fuel(m):
    f = math.floor(int(m)/3) - 2
    if f <= 0: return 0
    return f + get_fuel(f)

inp = FileImporter.get_input("/../input/1.txt").split("\n")


print(sum(get_fuel(int(i)) for i in inp))
