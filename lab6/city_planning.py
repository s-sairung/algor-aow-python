from object import Place
from object import City
import os
import math as m


def initialize_single_source(city: City, source: Place):
    for p in city.poi:
        p.distance = m.inf
        p.predecessor = None
    source.distance = 0


def relax(u: Place, v: Place, w: list):
    if v.distance > u.distance + w[u.id - 1][v.id - 1]:
        v.distance = u.distance + w[u.id - 1][v.id - 1]
        v.predecessor = u


def extract_min(l: list[Place]):
    min_distance = m.inf
    min_place_index = -1
    for i in range(len(l)):
        if l[i].distance < min_distance:
            min_distance = l[i].distance
            min_place_index = i
    temp = l[min_place_index]
    l.pop(min_place_index)
    return temp


global path
path = ''
def print_all_pair_path(i: Place, j: Place):
    pre = j.predecessor
    global path
    if i == j:
        path = path + str(i.id)

    elif pre == None:
        # print('nein mai naaa!') 
        return False
    else:
        print_all_pair_path(i, pre)
        path = path + str(j.id)


def check_all_pair_path(i: Place, j: Place):
    pre = j.predecessor
    if i == j:
        return True
    elif pre == None:
        return False
    check_all_pair_path(i, pre)


def dijkstraaaa(city: City, source: Place):
    w = city.adjMatrix
    initialize_single_source(city, source)
    s = set()
    l = city.poi.copy()
    while len(l) != 0:
        u = extract_min(l)
        s.add(u)
        # s = s.union({u})
        # https://www.w3schools.com/python/python_sets_methods.asp
        for j in range(len(w[u.id - 1])):
            if w[u.id - 1][j] != 0:
                v = city.poi[j]
                relax(u, v, w)


def build_city(s: list):
    a = int(s[0])
    b = int(s[1])
    if a == 0 and b == 0: return None
    c = City(a, b)
    return c


def check_city(c: City, u: Place):
    for v in c.poi: # O(V**2)
        path_found = check_all_pair_path(u, v) # O(V)
        if path_found == False:
            return False
    return True

"""----------------------------อ่านไฟล์อยู่นี่ค่ะ-------------------------------------"""
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/test.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()


first_time = True
city_map = []
for line in lines: # line = ['0 1']
    s = line.split() # s = ['0', '1']

    if len(s) == 2 and first_time:
        c = build_city(s)
        if c == None: break
        first_time = False

    elif len(s) == 2 and not first_time:
        city_map.append(c)
        c = build_city(s)
        if c == None: break

    elif len(s) == 3:
        c.build_road(line)


global time
global comps
global last
def dfs(c: City, trans_mode: bool):
    global time
    global comps
    comps = []
    if trans_mode:
        poi = c.poi_sorted.copy()
    else:
        poi = c.poi.copy()
    for u in poi:
        u.color = 'WHITE'
        u.predecessor = None
    time = 0
    for u in poi:
        # print('transmode = ' + str(trans_mode))
        # print('u.id = ' + str(u.id))
        if u.color == 'WHITE':
            dfs_visit(c, u, trans_mode)
            if trans_mode:
                comps.append(u)
                print('u.id = ' + str(u.id))


def dfs_visit(c: City, u: Place, trans_mode: bool):
    if trans_mode:
        w = c.adjMatrixTrans.copy()
    else:
        w = c.adjMatrix.copy()
    global time
    time = time + 1
    u.distance = time
    u.color = 'GRAY'
    for j in range(len(w[u.id - 1])):
        if w[u.id - 1][j] != 0:
            v = c.poi[j]
            if v.color == 'WHITE':
                v.predecessor = u
                dfs_visit(c, v, trans_mode)
    u.color = 'BLACK'
    time = time + 1
    u.finished = time


def selection_sort_place_des(c: City):
    l = c.poi.copy()
    adj = c.adjMatrixTrans.copy()
    for i in range(len(l) - 1):
        minimum = i
        for j in range(len(l) - 1, i, - 1):
            min_p = l[minimum].finished
            cur_p = l[j].finished
            if (cur_p > min_p):
                minimum = j
        if (minimum != i):
            l[i], l[minimum] = l[minimum], l[i]
            adj[i], adj[minimum] = adj[minimum], adj[i]

    for i in range(len(c.poi)):
        for j in range(len(l)):
            if c.poi[i].id == l[j].id:
                c.new_index[i] = j
                
    c.poi_sorted = l
    c.adjMatrixTrans_sorted = adj


def strongly_connected_components(c: City):
    dfs(c, False)
    # for p in c.poi:
    #     print('id = ' + str(p.id) + ' finish = ' + str(p.finished))
    selection_sort_place_des(c)
    dfs(c, True)


# city_map เก็บทุกเมืองที่สร้างเสร็จแล้ว
# city.poi เก็บสถานที่ทุกจุดในเมืองหนึ่ง ๆ

for city in city_map: # O(G V**3)
    for u in city.poi: # ไล่สร้าง dijkstraaaaa ทีละจุดจากทุกจุด O(V**3)
        dijkstraaaa(city, u) # O(V**2)
        path_found = check_city(city, u) # ไล่เช็ค path ระหว่างจุด u กับจุด v แต่ละจุดใน city O(V**2)
        if path_found == False:
            print('0')
            strongly_connected_components(city)
            print('components = ' + str(len(comps)))
            break
    if path_found:
        print('1')
        
