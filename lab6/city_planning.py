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
        # for v in w[u.id - 1]: # v is int
        #     relax(u, v, w)
        for j in range(len(w[u.id - 1])):
            if w[u.id - 1][j] != 0:
                v = city.poi[j]
                relax(u, v, w)


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/6.1.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()


first_time = True
city_map = []
for line in lines:
    s = line.split()

    if len(s) == 2 and first_time:
        a = int(s[0])
        b = int(s[1])
        if a == 0 and b == 0: break
        c = City(a, b)
        first_time = False

    elif len(s) == 3:
        c.build_road(line)

    elif len(s) == 2 and not first_time:
        city_map.append(c)
        a = int(s[0])
        b = int(s[1])
        if a == 0 and b == 0: break
        c = City(a, b)

for city in city_map:
    for u in city.poi:
        dijkstraaaa(city, u)
        for v in city.poi:
            # print('\nu = ' + str(u.id) + ' -> v = ' + str(v.id))
            path_found = print_all_pair_path(u, v)
            # print(path_found)
            # print(path)
            path = ''
            if path_found == False:
                print('0')
                break
        if path_found == False:
            break
    if path_found == None:
        print('1')
'''
c = None

for line in lines:
    s = line.split()
    if len(s) == 2 and c is None: # เมืองแรก
        print('First City')
        a = int(s[0])
        b = int(s[1])
        c = City(a, b)

    elif len(s) == 2 and c is not None: # เจอเมืองใหม่
        
        a = int(s[0])
        b = int(s[1])

        print('\nNew City')

        # คำนวณเมืองก่อนหน้านี้
        path_found = True
        for u in c.poi:
            dijkstraaaa(c, u)
            # วน print
            for v in c.poi:
                print('\nu = ' + str(u.id) + ' -> v = ' + str(v.id))
                print_all_pair_path(u, v)
                print(path)
                path = ''

        
        c = City(a, b)

    elif len(s) == 3:
        c.build_road(line)
'''

# วนทุกจุด
# for u in c.poi:
#     dijkstraaaa(c, u)
#     for v in c.poi:
#         print('u = ' + str(u.id) + ' -> v = ' + str(v.id))
#         print_all_pair_path(u, v)
#         print('---------')
#     print('-----------------')