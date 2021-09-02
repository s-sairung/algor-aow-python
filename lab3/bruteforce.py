def bruteforce(arr, k): #โดนเรียกจาก tester
    #passaway???
    #Variables Costructions
    global num_of_solutions
    num_of_solutions = 0
    global p_used
    p_used = []
    global max_pickup
    max_pickup = 0
    global ar_k
    ar_k = []
    global cur_pickup
    cur_pickup = 0
    global g_used
    g_used = []
    lower_k = 0 - int(k)
    while (lower_k <= k):
        ar_k.append(lower_k)
        lower_k += 1
    # print(ar_k)

    bruteforce_recursive(arr, -1)

    print("Output (Number of Solutions via Bruteforce) : " + str(num_of_solutions) + ".")
    

#หา G
def bruteforce_recursive(arr, index):
    global max_pickup
    global cur_pickup
    global num_of_solutions
    global p_used
    global g_used
    found = False
    cur_index = index + 1
    
    while cur_index < len(arr):
        if arr[cur_index] == 'G':
            found = True
            break
        cur_index += 1

    if not found:
        # print("p_used = " + str(p_used))
        # print("g_used = " + str(g_used))
        if len(p_used) != 0 and len(g_used) != 0:
            p_used.pop(len(p_used) - 1)
            g_used.pop(len(g_used) - 1)
            cur_pickup -= 1
        if  cur_pickup == max_pickup:
            num_of_solutions += 1
        elif cur_pickup > max_pickup:
            max_pickup = cur_pickup
            num_of_solutions = 1
        return

    # ตรงนี้คือ found
    
    for n in ar_k:
        i = cur_index + n
        if i >= 0 and i < len(arr) and arr[i] == 'P' and i not in p_used:
            p_used.append(i)
            g_used.append(cur_index)
            cur_pickup += 1
            bruteforce_recursive(arr, cur_index)

    bruteforce_recursive(arr, cur_index)
    
