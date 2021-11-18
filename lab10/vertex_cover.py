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

def swkOrder_function(adj_matrix):
    # print Yes No
    boo = []
    for w in vertex_combinations:
        boo.append(is_vertex_cover(w, adj_matrix))

    if True in boo:
        print("Yeah Suay!")
    else:
        print("No Way")

    # print answers
    ans = ""
    for w in vertex_combinations:
        if is_vertex_cover(w, adj_matrix):
            for a in w:
                print(a, end = " ")
            print()
        # mairu mairu khob khun kub suay!

    
# print(aprox_vertex_cover(adj_matrix))

def swkPreOrder_function(adj_matrix):
    ans = ""
    answer = []
    cnt = 0
    for w in aprox_vertex_cover(adj_matrix):
        for a in w:
            cnt += 1
            ans = ans + str(a) 
    print(cnt)

    for s in sorted(ans):
        print(s, end = " ")
    print()


print("-----------------No.1-----------------")
swkOrder_function(adj_matrix)
print("-----------------No.2-----------------")
swkPreOrder_function(adj_matrix)
print("-----------------No.3-----------------")

clauses = 1
literals = [[1, -2, 3]]

def reduction(clauses: int, literals: list):
    # หาจำนวน variable
    vars = set()
    for l in literals:
        for v in l:
            vars.add(abs(v))
    
    n = len(vars) # จำนวน variables
    m = clauses # จำนวน clauses
    vertices = 2*n + 3*m # จำนวนจุดทั้งหมด
    k = n + 2*m # ค่า K

    adj = [[0] * vertices for i in range(vertices)]
    
    top_graph = 2*n
    bottom_graph = 3*m
    
    # สร้างกราฟส่วนบน
    
    top_edges = []
    for i in range(top_graph):
        if i%2 == 0:
            top_edges.append((i, i+1))

    for e in top_edges:
        i = e[0]
        j = e[1]
        adj[i][j] = 1
        adj[j][i] = 1
                
    # print(adj)
    
    # สร้างกราฟส่วนล่าง

    for h in range(top_graph, top_graph + bottom_graph, 3):
        for i in range(h, h + 3):
            for j in range(h, h + 3):
                if i != j:
                    adj[i][j] = 1
                
    
        
    # เชื่อมกราฟบนกับล่าง (clause เดียว)

    cur_clause = 0
    for h in range(top_graph, top_graph + bottom_graph, 3):
        for i in range(len(literals[cur_clause])): # clauses[cur_clause] -> [x1, -x2, x3]
            l = literals[cur_clause][i]
            v = abs(l)
            if l >= 0:
                # print('l+; ' + str((v - 1)*2) + ', ' + str(i + h))
                adj[(v - 1)*2][i + h] = 1
                adj[i + h][(v - 1)*2] = 1
            else:
                # print('l-; ' + str((v - 1)*2 + 1) + ', ' + str(i + h))
                adj[(v - 1)*2 + 1][i + h] = 1
                adj[i + h][(v - 1)*2 + 1] = 1
        cur_clause += 1
    
    # susususu
    # print(adj)
    return (vertices, k, adj)

vertices_reduce, k_reduce, adj_reduce = reduction(clauses, literals)
print(vertices_reduce)
print(k_reduce)
for l in adj_reduce:
    print(l)



    