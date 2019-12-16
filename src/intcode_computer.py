from collections import defaultdict

class IntcodeComputer:
    def __init__(self, prog, inputs = []):
        self.inputs = inputs

        self.prog = defaultdict(int)
        self.prog.update({i: item for i, item in enumerate(prog)})

        self.halted = False
        self.i = 0
        self.last_output = None
        self.r_base = 0

    def clone(self):
        n = IntcodeComputer([self.prog[i] for i in range(len(self.prog))])
        n.inputs = self.inputs[:]
        n.halted = self.halted
        n.i = self.i
        n.last_output = self.last_output
        n.r_base = self.r_base
        return n

    def get_val(self, prog, i, mode):
        ''' Used to get value of an address for reading purposes '''
        if mode == '0':
            return prog[prog[i]]
        if mode == '1':
            return prog[i]
        if mode == '2':
            return prog[self.r_base + prog[i]]
        raise Exception("Invalid mode")

    def get_address(self, i, mode):
        ''' Used to get address index for writing purposes. Does not support immediate mode. '''
        if mode == '0':
            return i
        if mode == '2':
            return self.r_base + i
        raise Exception("Invalid mode")
    
    def get_output(self):
        while self.i < len(self.prog):

            if self.prog[self.i] == 99: 
                self.halted = True
                break

            instruction = str(self.prog[self.i]).rjust(5, '0')
            modes, op = instruction[:3], instruction[3:]

            if op == "01":
                a, b = self.get_val(self.prog, self.i+1, modes[2]), self.get_val(self.prog, self.i+2, modes[1])
                self.prog[self.get_address(self.prog[self.i+3], modes[0])] = a + b
                self.i += 4
                
            elif op == "02":
                a, b = self.get_val(self.prog, self.i+1, modes[2]), self.get_val(self.prog, self.i+2, modes[1])
                self.prog[self.get_address(self.prog[self.i+3], modes[0])] = a * b
                self.i += 4

            elif op == "03":
                if len(self.inputs) == 0:
                    return None
                    
                a = self.prog[self.i+1]
                self.prog[self.get_address(a, modes[2])] = self.inputs.pop(0)
                self.i += 2

            elif op == "04":
                a = self.get_val(self.prog, self.i+1, modes[2])
                self.i += 2
                self.last_output = a
                return a

            elif op == "05":
                a = self.get_val(self.prog, self.i+1, modes[2])
                if a != 0:
                    self.i = self.get_val(self.prog, self.i+2, modes[1])
                else:
                    self.i += 3

            elif op == "06":
                a = self.get_val(self.prog, self.i+1, modes[2])
                if a == 0:
                    self.i = self.get_val(self.prog, self.i+2, modes[1])
                else:
                    self.i += 3

            elif op == "07":
                a, b = self.get_val(self.prog, self.i+1, modes[2]), self.get_val(self.prog, self.i+2, modes[1])
                self.prog[self.get_address(self.prog[self.i+3], modes[0])] = 1 if a < b else 0
                self.i += 4

            elif op == "08":
                a, b = self.get_val(self.prog, self.i+1, modes[2]), self.get_val(self.prog, self.i+2, modes[1])
                self.prog[self.get_address(self.prog[self.i+3], modes[0])] = 1 if a == b else 0
                self.i += 4

            elif op == "09":
                a = self.get_val(self.prog, self.i+1, modes[2])
                self.r_base += a
                self.i += 2
            
            else:
                raise Exception("Bad code!")