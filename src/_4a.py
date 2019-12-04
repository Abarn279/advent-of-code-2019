from file_importer import FileImporter

# Conditions
is_six = lambda x: len(x) == 6
has_adjacent = lambda x: any(x[i] == x[i+1] for i in range(len(x) - 1))
is_ascending = lambda x: all(int(x[i]) <= int(x[i+1]) for i in range(len(x) - 1))

low, high = map(int, FileImporter.get_input("/../input/4.txt").split("-"))

print(sum(1 for pw in range(low, high + 1) if is_six(str(pw)) and has_adjacent(str(pw)) and is_ascending(str(pw))))
