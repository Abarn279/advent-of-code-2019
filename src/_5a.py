from file_importer import FileImporter

def get_val(prog, i, mode):
    if mode == '0':
        return prog[i]
    if mode == '1':
        return i
    raise Exception("Invalid mode")

def op1(prog, a, b, c):
    prog[c] = prog[a] + prog[b]
    return 4

def op2(prog, a, b, c):
    prog[c] = prog[a] * prog[b]
    return 4

def op3(prog, a): 
    prog[a] = 1
    return 2

def op4(prog, a):
    print(prog[a])
    return 2

prog = list(map(int, FileImporter.get_input("/../input/5.txt").split(",")))

i = 0
while i < len(prog):

    if prog[i] == 99: break

    instruction = str(prog[i]).rjust(5, '0')
    modes, op = instruction[:3], instruction[3:]

    if op == "01":
        i += op1(prog, get_val(prog, i+1, modes[2]), get_val(prog, i+2, modes[1]), get_val(prog, i+3, modes[0]))
        
    elif op == "02":
        i += op2(prog, get_val(prog, i+1, modes[2]), get_val(prog, i+2, modes[1]), get_val(prog, i+3, modes[0]))

    elif op == "03":
        i += op3(prog, get_val(prog, i+1, modes[2]))

    elif op == "04":
        i += op4(prog, get_val(prog, i+1, modes[2]))
