from file_importer import FileImporter
from collections import deque

def deal_into_new(deck): 
    return deque(reversed(deck))

def cut_n(deck, n):
    deck.rotate(-n)

def deal_with_inc(deck, inc):
    table = [None for i in range(len(deck))]
    i = 0
    while len(deck) > 0:
        table[i] = deck.popleft()
        i = (i + inc) % len(table)
    return deque(table)


inp = FileImporter.get_input("/../input/22.txt").split("\n")
deck = deque(list(range(10007)))

for i in inp:
    if i[:9] == "deal into":
        deck = deal_into_new(deck)
    elif i[:9] == "deal with":
        deck = deal_with_inc(deck, int(i.split(' ')[3]))
    elif i[:3] == "cut":
        cut_n(deck, int(i.split(' ')[1]))

print(deck.index(2019))
