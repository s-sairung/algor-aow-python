from pydantic import validate_arguments
import math as m
import os


@validate_arguments
def dist(p1: tuple, p2: tuple):
    return m.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


@validate_arguments
def cost(p1: tuple, p2: tuple, p3: tuple):
    return dist(p1, p2) + dist(p2, p3) + dist(p1, p3)


global points
global vertices
global cost_table
global k_table
cost_table = [[-1] * 2 for i in range(2)] # temp
k_table = [[-1] * 2 for i in range(2)] # temp


@validate_arguments
def min_cost(i: int, j: int):
    
    if cost_table[i][j] != -1:
        return cost_table[i][j]

    if i + 2 > j: # เช็คว่าเป็นเส้น
        cost_table[i][j] = 0
        return 0
    
    min_cost_temp = m.inf
    for k in range(i + 1, j):
        cost_temp = min_cost(i, k) + min_cost(k, j) + cost(vertices[i], vertices[k], vertices[j])
        if cost_temp < min_cost_temp:
            min_cost_temp = cost_temp
            k_table[i][j] = k

    cost_table[i][j] = min_cost_temp
    return min_cost_temp


def pipeswk_ordered():
    print('-----Cost-Table-----')
    i = 0
    for pipeswk in cost_table:
        print(str(i) + ' ' + str(pipeswk))
        i += 1

def print_k():
    print('------K-Table------')
    i = 0
    for line in k_table:
        print(str(i) + ' ' + str(line))
        i += 1

   
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/2.1.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()

points = int(lines[0])
vertices = []
for i in range(1, len(lines)):
    x, y = lines[i].split()
    x = float(x)
    y = float(y)
    vertices.append((x, y))

# vertices = [(0, 0), (1, 0), (2, 1), (1, 2), (0, 2)]
# points = 5

cost_table = [[-1] * points for i in range(points)]
k_table = [[-1] * points for i in range(points)]

print('Input: ' + str(vertices) + ' (points = ' + str(points) + ')')
print('คำตอบของคำถามที่อาจารย์ถามมาที่ว่านั้นก็คื้อออออออ: ' + str(min_cost(0, points - 1)) + ' นั่นเองเองเองเอง!!!!')

pipeswk_ordered()
print_k()
