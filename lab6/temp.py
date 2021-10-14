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