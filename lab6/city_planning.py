from object import Place
from object import City
import os
import math as m
import random


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
global comp_root
global last
global comp_member
global temp

def dfs(c: City, trans_mode: bool):
    global time
    global comp_root
    global comp_member
    global temp
    comp_root = []
    comp_member = []
    temp = []
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
                comp_root.append(u)
                comp_member.append(temp)
                temp = []
                # print('u.id = ' + str(u.id))


def dfs_visit(c: City, u: Place, trans_mode: bool):
    global temp
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

    if trans_mode:
        temp.append(u)  
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
            print('components = ' + str(len(comp_member)))

            # print comp_member = [[p1, p2], [p3], [p4, p5, p6]]
            '''
            for i in range(len(comp_member)):
                print('member number ' + str(i+1))
                for p in comp_member[i]:
                    print(p.id, end=' ')
                print('')
            '''

            # idealy best algorithm for joining components for us -zaragapoy
            '''
            comp_member_temp = comp_member.copy()
            while len(comp_member_temp) > 1:
                i1 = random.randrange(len(comp_member_temp))
                i2 = random.randrange(len(comp_member_temp))
                while i2 == i1:
                    i2 = random.randrange(len(comp_member_temp))
                c1 = comp_member_temp[i1]
                c2 = comp_member_temp[i2]
                print('build expressway: ' + str(c1[0].id) + ' <-> ' + str(c2[0].id))
                c1.extend(c2)
                comp_member_temp.pop(i2)
            print('new components = ' + str(len(comp_member_temp)))
            '''
            
            comp_member_temp = comp_member.copy() # comp_member_temp = [[p1, p2], [p3], [p4, p5, p6]]
            big_comp = comp_member_temp[0].copy() # inner SCCs
            
            # 1. loop จนกว่าขนาดของ big_comp = จำนวนจุด
            # 2. ไล่เช็กแต่ละ SCC
            # 3. ไล่เช็กแต่ละ จุดที่อยู่ใน SCC หนึ่ง ๆ
            # 4. ดูว่าแต่ละจุดนั้นเชื่อมไป SCC อื่นไหม
            #   4.1 ถ้าเชื่อมไป SCC อื่น และ SCC นั้นไม่อยู่ใน big_comp เพิ่ม SCC นั้นลง big_comp แสดงเส้นเชื่อมใหม่
            #   4.2 ถ้าเชื่อมไป SCC อื่น แต่ SCC นั้นอยู่ใน big_comp ข้ามไป (continue)
            #   4.3 ถ้าเชื่อมไป SCC เดิม ให้ continue
            # 5. ถ้าทำจนครบแล้วแต่ big_comp != จำนวนจุด นั้นคือ มี SCC(s) ที่แยกกันอยู่อย่างสมบูรณ์ ให้สร้างทาง ไป-กลับ ให้ทั้งสอง SCC นั้น
            #    จนกว่า big_comp = จำนวนจุด
            
            for i in range(len(comp_member_temp)): # for each SCCs 
                for j in range(len(comp_member_temp[i])): # for each point in SCCs
                    p = comp_member_temp[i][j]
                    p_adj = city.adjMatrix[p.id - 1]
                    for k in range(len(p_adj)): # เช็กว่าจุดปัจจุบันมีเส้นเชื่อมกับจุดอื่นมั้ย
                        if p_adj[k] == 1:
                            if city.poi[k] not in big_comp and city.poi[k] not in comp_member_temp[i]:
                                for g in range(len(comp_member_temp)):
                                    if city.poi[k] in comp_member_temp[g]:
                                        big_comp.extend(comp_member_temp[g])
                                        break
                                print("suggested new road plan : " + str(city.poi[k].id) + " -> " + str(p.id))
                            else:
                                continue
            
            if len(big_comp) != len(city.poi):
                for comp in comp_member_temp:
                    if comp[0] not in big_comp:
                        print("suggested new road plan : " + str(comp[0].id) + " -> " + str(big_comp[0].id))       
            break
     
    if path_found:
        print('1')
        
