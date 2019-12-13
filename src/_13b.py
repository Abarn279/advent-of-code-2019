from file_importer import FileImporter
from intcode_computer import IntcodeComputer
from tkinter import Canvas, mainloop, Tk
from aoc_utils import Vector2
from time import sleep
import random
import math

class Tile:
    def __init__(self, x, y, id):
        self.pos = Vector2(x, y)
        self.id = id
    def __hash__(self):
        return hash(f'{self.pos.x},{self.pos.y},{self.id}')

def get_color(id):
    if id == 0:
        return '#000000'
    else:
        return '#FFFFFF'

prog = list(map(int, FileImporter.get_input("/../input/13.txt").split(",")))
prog[0] = 2

# Setup gui and canvas
gui = Tk()
c_height = 1000
c_width = 1000
canvas = Canvas(gui, width=1000, height=1000)
canvas.pack()

# Size of each grid item
point_size = 20

# Get a point for the canvas (scaled and offset)
get_canvas_point = lambda vec2: Vector2((vec2.x * point_size) + point_size, (vec2.y * point_size) + point_size)

computer = IntcodeComputer(prog)

tiles = {}
score = 0
while True:
    canvas.delete("all")

    # Set joystick
    joystick = 0
    if len(tiles) > 0:
        [ball] = [i for i in tiles.items() if i[1].id == 4]
        [paddle] = [i for i in tiles.items() if i[1].id == 3]

        if ball[1].pos.x < paddle[1].pos.x:
            joystick = -1
        elif ball[1].pos.x > paddle[1].pos.x:
            joystick = 1

    computer.inputs = [joystick]

    # Get updates for tiles from computer
    while not computer.halted:
        x, y, id = [computer.get_output() for _ in range(3)]

        if x == -1 and y == 0:
            score = id
            continue

        if any(i is None for i in [x, y, id]):
            break
        
        tiles[x, y] = Tile(x, y, id)

    # Set tiles to canvas
    for tile in tiles.values():
        canvas_point = get_canvas_point(tile.pos)
        canvas.create_rectangle(canvas_point.x, canvas_point.y, canvas_point.x + point_size, canvas_point.y + point_size, fill = get_color(tile.id))
    canvas.create_text(500,500,font="Times 20 italic bold", text=score)

    canvas.update_idletasks()
    canvas.update()

