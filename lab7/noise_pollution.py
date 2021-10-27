#                           |
#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| ; ; |)
#                       0\  o  /0
#                     __;/`---'\;__
#                   .' \|     |// '.
#                  / \|||  :  |||// \
#                 / _||||| -:- |||||- 
#                |   | \\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
#
#                       สาธุ คืนเดียวเสร็จ
#

import os
import copy
import math as m

class Vertice:

    def __init__(self, id: int):
        self.id = id


class Matrix:
    
    def __init__(self, k: int, n: int):
        self.k = k
        self.matrix = [[m.inf] * n for i in range(n)]

    def rows(self):
        return len(self.matrix)

    def copy_matrix(self):
        return copy.deepcopy(self.matrix)

    


def floyd_warshall(w: list):
    n = len(w)

    # initialize pi0
    pi0 = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or w[i][j] == m.inf:
                pi0[i][j]= None #cryyyy
            else:
                pi0[i][j] = i

    d0 = copy.deepcopy(w)
    arr_d = []
    arr_d.append(d0)
    arr_pi = []
    arr_pi.append(pi0)
    for k in range(1, n + 1):
        d = [[m.inf] * n for i in range(n)]
        pik = [[None] * n for i in range(n)]
        for i in range(n): 
            for j in range(n):
                d[i][j] = min(arr_d[k - 1][i][j], arr_d[k - 1][i][k - 1] + arr_d[k - 1][k - 1][j])
                if arr_d[k - 1][i][j] <= arr_d[k - 1][i][k - 1] + arr_d[k - 1][k - 1][j]:
                    pik[i][j] = arr_pi[k - 1][i][j]
                else:
                    pik[i][j] = arr_pi[k - 1][k - 1][j]
        arr_d.append(d)
        arr_pi.append(pik)
    return (arr_d[n], arr_pi[n])


def print_all_pair_shortest_path(pi: list, i: int, j: int):
    if i == j:
        print(i + 1)
    elif pi[i][j] == None:
        print("no path jaaa")
    else:
        print_all_pair_shortest_path(pi, i, pi[i][j])
        print(j + 1)

"""----------------------------อ่านไฟล์อยู่นี่ค่ะ-------------------------------------"""
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/7.1.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()
print(lines)

vertices, edges, ans = lines[0].split(" ")
vertices = int(vertices)
edges = int(edges)
ans = int(ans)
weight_matrix = [[m.inf] * vertices for i in range(vertices)]

# w.matrix[1 - 1][2 - 1] = 20

for line in range(1, edges + 1):
    i, j, w = lines[line].split(" ")
    i = int(i)
    j = int(j)
    w = int(w)
    weight_matrix[i - 1][j - 1] = w
    # weight_matrix[j - 1][i - 1] = w # undirected graph
    
print(weight_matrix)
tup = floyd_warshall(weight_matrix)
print(tup[0])
print(tup[1])

for line in range(edges + 1, edges + ans + 1):
    i, j = lines[line].split(" ")
    print("Path for i = " + i + ", j = " + j)
    i = int(i) - 1
    j = int(j) - 1
    print_all_pair_shortest_path(tup[1], i, j)
    print("----------")