from file_importer import FileImporter
import math
from collections import defaultdict

def roundup(x, y):
    ''' Rounds x up to nearest y '''
    return x if x % y == 0 else x + y - x % y

class ReactionComponent:
    def __init__(self, chemical_id, number):
        self.chemical_id = chemical_id; self.number = number
    def __repr__(self):
        return f'{str(self.number)} {self.chemical_id}'

class Reaction:
    def __init__(self, inputs: list, output: ReactionComponent):
        self.inputs = inputs; self.output = output
    def __repr__(self):
        return f'{self.inputs} => {self.output}'

def produce(chemical_id, amount, amounts_map):
    global reactions
    [produce_reaction] = [i for i in reactions if i.output.chemical_id == chemical_id]

    if amount < produce_reaction.output.number:
        amount = produce_reaction.output.number
    multiple = amount // produce_reaction.output.number
    remainder = amount % produce_reaction.output.number

    total_ore = 0
    inp_i = 0
    while inp_i != len(produce_reaction.inputs):    # Loop through all the inputs, reducing the amount of that 
        inp = produce_reaction.inputs[inp_i]        # chemical we have by the amount of the input, and producing the output

        required_amount = inp.number * multiple
        if amounts_map[inp.chemical_id] >= required_amount:  # We have enough of this particular reaction input
            amounts_map[inp.chemical_id] -= required_amount
            inp_i += 1

        else:                                       # Need to produce more
            existing = amounts_map[inp.chemical_id]
            need_to_produce = required_amount - existing
            
            if inp.chemical_id == "ORE":
                amounts_map["ORE"] += need_to_produce    # Base case for ORE
                total_ore += need_to_produce
            else:
                total_ore += produce(inp.chemical_id, need_to_produce, amounts_map)

    amounts_map[produce_reaction.output.chemical_id] += multiple * produce_reaction.output.number
    if remainder > 0:
        total_ore += produce(chemical_id, remainder, amounts_map)

    return total_ore


# Get input and set up reactions based on it
reactions_inp = FileImporter.get_input("/../input/14.txt").split("\n")
reactions = []
for r in reactions_inp:
    inp_s, outp_s = r.split(" => ")

    inputs = []
    for i in inp_s.split(', '):
        num, chem = i.split(' ')
        rc = ReactionComponent(chem, int(num))
        inputs.append(rc)
    num, chem = outp_s.split(' ')
    output = ReactionComponent(chem, int(num))
    reactions.append(Reaction(inputs, output))

def b_search():
    l = 0
    r = 1000000000000
    while l < r:
        amounts = defaultdict(int)

        m = math.floor((l + r) / 2)

        ore_used = produce("FUEL", m, amounts)

        if ore_used < 1000000000000:
            l = m + 1
        elif ore_used > 1000000000000:
            r = m - 1
        else:
            return m

    return l

print(b_search())
