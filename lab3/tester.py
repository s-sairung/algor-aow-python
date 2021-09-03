import os
from bruteforce import bruteforce
from greedy import greedy

# open file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/Extra/3.4.5.txt')
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


# k = 1
# arr = ['P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P']

print("Input : arr [] = " + str(arr) + "; k = " + str(k) + ".")

bruteforce(arr, k)
greedy(arr, k)
#susu /.ชูป้ายไฟ เก่งม้าก