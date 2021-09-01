import os

# open file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/Example/3.1.2.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()

#print(lines)

input_line_1 = lines[0]
input_line_2 = lines[1]
arr = []

# input_line_1 = "GGPPGGGGPPPG"
# input_line_2 = 3
# arr = []

# construct array from input file
k = int(input_line_2)
for c in input_line_1:
    arr.append(c)

print("Input : arr [] = " + str(arr) + ",\n\t\tk = " + str(k) + ".")

index_taken = []
max_passenger = 0

for i in range(len(arr)):
    if arr[i] == 'G':
        start = i - k
        end = i + k
        for j in range(start, end+1):
            if j >= 0 and j < len(arr) and arr[j] == 'P' and j not in index_taken:
                index_taken.append(j)
                max_passenger += 1
                break

print("Output : " + str(max_passenger) + ".")