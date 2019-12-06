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

inp = [i.split(')') for i in FileImporter.get_input("/../input/6.txt").split("\n")]

objs = {}

for obj, orbiting in inp:
    if obj not in objs:
        objs[obj] = Obj(obj)
    if orbiting not in objs:
        objs[orbiting] = Obj(orbiting)
    objs[obj].orbiting.append(objs[orbiting])
    objs[orbiting].parent = objs[obj]

print(sum(objs[i].get_depth() for i in objs.keys()))