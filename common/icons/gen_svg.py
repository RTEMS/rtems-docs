#!/usr/bin/env python3
import os

map = []
with open("list.txt", "r") as fp:
    for line in fp.read().splitlines():
        colour, text = line.split("	")
        map.append([colour, text])

with open("base.svg", "r") as fp:
    base = fp.read()

os.makedirs("png", exist_ok=True)
for colour, text in map:
    filename = "icons/{}.svg".format(text.lower())
    with open(filename, "w") as fp:

        icon = base.replace("RP-TEXT", text)
        icon = icon.replace("RP-COLOUR", colour)
        icon = icon.replace("RP-FILENAME", text.lower())

        fp.write(icon)
