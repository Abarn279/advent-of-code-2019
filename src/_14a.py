from file_importer import FileImporter
import math
from collections import defaultdict

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

    total_ore = 0
    inp_i = 0
    while inp_i != len(produce_reaction.inputs):    # Loop through all the inputs, reducing the amount of that 
        inp = produce_reaction.inputs[inp_i]        # chemical we have by the amount of the input, and producing the output

        required_amount = inp.number * amount
        if amounts_map[inp.chemical_id] >= required_amount:  # We have enough of this particular reaction input
            amounts_map[inp.chemical_id] -= required_amount
            inp_i += 1

        else:                                       # Need to produce more
            while amounts_map[inp.chemical_id] < required_amount:

                if inp.chemical_id == "ORE":
                    amounts_map["ORE"] += required_amount    # Base case for ORE
                    total_ore += required_amount
                else:
                    total_ore += produce(inp.chemical_id, amount, amounts_map)        # If not ORE, recurse

    amounts_map[produce_reaction.output.chemical_id] += produce_reaction.output.number * amount
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

# map of chemical id to how much we currently have of it
amounts = defaultdict(int)
total_ore = produce("FUEL", 1, amounts)
print(total_ore)
