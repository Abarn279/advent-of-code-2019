from file_importer import FileImporter

def get_val(prog, i, mode):
    if mode == '0':
        return prog[prog[i]]
    if mode == '1':
        return prog[i]
    raise Exception("Invalid mode")

prog = list(map(int, FileImporter.get_input("/../input/5.txt").split(",")))

i = 0
while i < len(prog):

    if prog[i] == 99: break

    instruction = str(prog[i]).rjust(5, '0')
    modes, op = instruction[:3], instruction[3:]

    if op == "01":
        a, b = get_val(prog, i+1, modes[2]), get_val(prog, i+2, modes[1])
        prog[prog[i+3]] = a + b
        i += 4
        
    elif op == "02":
        a, b = get_val(prog, i+1, modes[2]), get_val(prog, i+2, modes[1])
        prog[prog[i+3]] = a * b
        i += 4

    elif op == "03":
        a = prog[i+1]
        prog[a] = int(input("Input ID: "))
        i += 2

    elif op == "04":
        a = get_val(prog, i+1, modes[2])
        print(a)
        i += 2

    elif op == "05":
        a = get_val(prog, i+1, modes[2])
        if a != 0:
            i = get_val(prog, i+2, modes[1])
        else:
            i += 3

    elif op == "06":
        a = get_val(prog, i+1, modes[2])
        if a == 0:
            i = get_val(prog, i+2, modes[1])
        else:
            i += 3

    elif op == "07":
        a, b = get_val(prog, i+1, modes[2]), get_val(prog, i+2, modes[1])
        prog[prog[i+3]] = 1 if a < b else 0
        i += 4

    elif op == "08":
        a, b = get_val(prog, i+1, modes[2]), get_val(prog, i+2, modes[1])
        prog[prog[i+3]] = 1 if a == b else 0
        i += 4
    
    else:
        raise Exception("Bad code!")