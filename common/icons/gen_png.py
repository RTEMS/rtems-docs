#!/usr/bin/env python3
import os
import subprocess

map = []
with open("list.txt", "r") as fp:
    for line in fp.read().splitlines():
        colour, text = line.split("	")
        map.append([colour, text])

os.makedirs("png", exist_ok=True)
for colour, text in map:
    filename = text.lower()

    file_in = "icons/{}.svg".format(filename)
    file_out = "png/{}.png".format(filename)

    cmd = ["inkscape", file_in, "-o", file_out]

    print("GENERATING:", file_out)
    subprocess.run(cmd)
