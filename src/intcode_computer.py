class IntcodeComputer:
    def __init__(self, prog, inputs):
        self.inputs = inputs
        self.prog = prog

    def get_val(self, prog, i, mode):
        if mode == '0':
            return prog[prog[i]]
        if mode == '1':
            return prog[i]
        raise Exception("Invalid mode")
    
    def get_output(self):
        i = 0
        while i < len(self.prog):

            if self.prog[i] == 99: break

            instruction = str(self.prog[i]).rjust(5, '0')
            modes, op = instruction[:3], instruction[3:]

            if op == "01":
                a, b = self.get_val(self.prog, i+1, modes[2]), self.get_val(self.prog, i+2, modes[1])
                self.prog[self.prog[i+3]] = a + b
                i += 4
                
            elif op == "02":
                a, b = self.get_val(self.prog, i+1, modes[2]), self.get_val(self.prog, i+2, modes[1])
                self.prog[self.prog[i+3]] = a * b
                i += 4

            elif op == "03":
                a = self.prog[i+1]
                self.prog[a] = self.inputs.pop(0)
                i += 2

            elif op == "04":
                a = self.get_val(self.prog, i+1, modes[2])
                return a
                i += 2

            elif op == "05":
                a = self.get_val(self.prog, i+1, modes[2])
                if a != 0:
                    i = self.get_val(self.prog, i+2, modes[1])
                else:
                    i += 3

            elif op == "06":
                a = self.get_val(self.prog, i+1, modes[2])
                if a == 0:
                    i = self.get_val(self.prog, i+2, modes[1])
                else:
                    i += 3

            elif op == "07":
                a, b = self.get_val(self.prog, i+1, modes[2]), self.get_val(self.prog, i+2, modes[1])
                self.prog[self.prog[i+3]] = 1 if a < b else 0
                i += 4

            elif op == "08":
                a, b = self.get_val(self.prog, i+1, modes[2]), self.get_val(self.prog, i+2, modes[1])
                self.prog[self.prog[i+3]] = 1 if a == b else 0
                i += 4
            
            else:
                raise Exception("Bad code!")