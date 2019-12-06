from file_importer import FileImporter

class Obj:
    def __init__(self, key):
        self.key = key
        self.orbiting = []
        self.parent = None
    def __repr__(self):
        return self.key
    def get_depth(self):
        if self.parent is not None:
            return 1 + self.parent.get_depth()
        return 0
    def get_parents(self):
        if self.parent == None: return []
        return [self.parent] + self.parent.get_parents()
    def get_distance_to_parent(self, parent):
        if self.parent == parent:
            return 1
        return 1 + self.parent.get_distance_to_parent(parent)

def get_first_shared_parent(youparents, sanparents):
    for i in youparents:
        for j in sanparents:
            if i == j:
                return i

inp = [i.split(')') for i in FileImporter.get_input("/../input/6.txt").split("\n")]

# Build orbits
objs = {}
for obj, orbiting in inp:
    if obj not in objs:
        objs[obj] = Obj(obj)
    if orbiting not in objs:
        objs[orbiting] = Obj(orbiting)
    objs[obj].orbiting.append(objs[orbiting])
    objs[orbiting].parent = objs[obj]

# Objects that YOU and SAN are orbiting
youorbiting = objs['YOU'].parent
sanorbiting = objs['SAN'].parent

# Get a list of parents for each of those objects
youparents = youorbiting.get_parents()
sanparents = sanorbiting.get_parents()

# Find first shared parent between the two
firstSharedParent = get_first_shared_parent(youparents, sanparents)

# Add up the distances between both to shared parent
print(youorbiting.get_distance_to_parent(firstSharedParent) + sanorbiting.get_distance_to_parent(firstSharedParent))

