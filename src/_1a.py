from file_importer import FileImporter
import math

inp = FileImporter.get_input("/../input/1.txt").split("\n")

print(sum(math.floor(int(i)/3) - 2 for i in inp))
