class IntcodeComputer:
    def __init__(self, prog, inputs):
        self.inputs = inputs
        self.prog = prog
        self.halted = False
        self.i = 0
        self.last_output = None

    def get_val(self, prog, i, mode):
        if mode == '0':
            return prog[prog[i]]
        if mode == '1':
            return prog[i]
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
                self.prog[self.prog[self.i+3]] = a + b
                self.i += 4
                
            elif op == "02":
                a, b = self.get_val(self.prog, self.i+1, modes[2]), self.get_val(self.prog, self.i+2, modes[1])
                self.prog[self.prog[self.i+3]] = a * b
                self.i += 4

            elif op == "03":
                a = self.prog[self.i+1]
                self.prog[a] = self.inputs.pop(0)
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
                self.prog[self.prog[self.i+3]] = 1 if a < b else 0
                self.i += 4

            elif op == "08":
                a, b = self.get_val(self.prog, self.i+1, modes[2]), self.get_val(self.prog, self.i+2, modes[1])
                self.prog[self.prog[self.i+3]] = 1 if a == b else 0
                self.i += 4
            
            else:
                raise Exception("Bad code!")