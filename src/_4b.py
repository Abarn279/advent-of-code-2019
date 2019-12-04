from file_importer import FileImporter

# Conditions
is_six = lambda x: len(x) == 6
is_ascending = lambda x: all(int(x[i]) <= int(x[i+1]) for i in range(len(x) - 1))

def has_adjacent(x):
    i = 0
    while i < len(x):
        num_same = 1
        for j in range(i + 1, len(x)):
            if x[j] == x[i]:
                num_same += 1
            else:
                break
        if num_same == 2:
            return True

        i += num_same
    return False

low, high = map(int, FileImporter.get_input("/../input/4.txt").split("-"))

print(sum(1 for pw in range(low, high + 1) if is_six(str(pw)) and has_adjacent(str(pw)) and is_ascending(str(pw))))
