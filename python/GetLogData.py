import os

filename = "test.txt"

with open(filename) as f:
    lines = set(f.read().splitlines())
    for line in lines:
        if "cincinnati" in lines:
            print(line)

# This file will output a line in a file that has Cincinnati in it.  This can be helpful to find certain log data