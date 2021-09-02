import os
from greedy import greedy

# open file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/Example/3.1.1.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()

# print(lines)

input_line_1 = lines[0]
input_line_2 = lines[1]
arr = []

k = int(input_line_2)
for c in input_line_1:
    arr.append(c)

greedy(arr, k)
