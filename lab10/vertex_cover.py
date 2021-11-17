import os
import random
import copy

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/ex1.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()

# print(lines)

k = int(lines[0])
print('k = ' + str(k))


adj_matrix = []

for i in range(1, len(lines)):
    adj_matrix.append([int(j) for j in lines[i].split(' ')])
    

print('adj = ' + str(adj_matrix))




def is_vertex_cover(w: list, adj: list):
    i = 0
    for u in adj:
        j = 0
        for v in u:
            if v == 1:
                if i + 1 not in w and j + 1 not in w:
                    return False
            j += 1
        i += 1
    return True
            
    
global vertex_combinations
vertex_combinations = []
def generate_combination():
    first_vertex = 1
    while (first_vertex <= len(adj_matrix)):
        combination = []
        combination.append(first_vertex)
        k_combination(combination)
        first_vertex = first_vertex + 1

global last_used
last_used = 0
def k_combination(comb: list):
    global last_used
    size = len(comb)
    ''' base case '''
    if size == 0:
        return
    if size == k:
        # print("combination :" + str(comb))
        vertex_combinations.append(copy.deepcopy(comb))
        last_used = comb.pop()
        return

    ''' recursive case '''
    for i in range(len(adj_matrix) + 1):
        if len(comb) == 0: return
        if i > comb[size - 1] and i > last_used:
            comb.append(i)
            k_combination(comb)
    last_used = comb.pop()
    return

'''
Aprox.
1) Initialize the result as {}
2) Consider a set of all edges in given graph.  Let the set be E.
3) Do following while E is not empty
...a) Pick an arbitrary edge (u, v) from set E and add 'u' and 'v' to result
...b) Remove all edges from E which are either incident on u or v.
4) Return result
5) Susuuuuuuu
'''

def aprox_vertex_cover(adj: list):
    w = []
    e = []
    i = 0
    for u in adj:
        j = 0
        for v in u:
            if v == 1:
                e.append((i + 1, j + 1))
            j += 1
        i += 1
    while len(e) != 0:
        edge = e[random.randrange(len(e))]
        u = edge[0]
        v = edge[1]
        w.append(edge)
        new_e = []
        for t in e:
            if u not in t and v not in t:
                new_e.append(t)
        e = new_e
    return w

generate_combination()
for w in vertex_combinations:
    print(w)
    print(is_vertex_cover(w, adj_matrix))
print(aprox_vertex_cover(adj_matrix))

