class bruteForce:

    # Reading input file
    """
    file = open("/input/Example/3.1.1.txt", "r")
    string = file.readline()
    integer = file.readline()
    file.close()
    """

    #Simulate input
    string = "GGPPGGGGPPPG"
    integer = "3"

    # Processing the input
    global arr
    arr = []
    for alphabet in string:
        arr.append(alphabet)
    global k
    k = int(integer)
    global max_pickup
    max_pickup = 0
    global used_index
    used_index = []
    global cnt
    cnt = 0

    # Pick up passenger in unit range
    def pick_up(index, unit):
        cnt_pick = 0
        p_index_left = index - unit
        p_index_right = index + unit
        if p_index_left >= 0 and arr[p_index_left] == "P" and not used_index.__contains__(p_index_left):
            used_index.append(p_index_left)
            cnt_pick += 1
        elif p_index_right < len(arr) and arr[p_index_right] == "P" and not used_index.__contains__(p_index_right):
            used_index.append(p_index_right)
            cnt_pick += 1
        return cnt_pick

    # Pairing Grab and Passenger
    for i in range(k):
        for j in range(len(arr)):
            if arr[j] == "G":
                cnt += pick_up(j,i)
        used_index.clear # WHY. DID. YOUUU. NOT. CLEAR. ALL. OF. YOUR. ITEMSSSSSSSSSS!!!!!!!!!
        if cnt > max_pickup:
            max_pickup = int(cnt)
            cnt = 0
             
    print("Output : " + str(max_pickup) + ".")

"""
 ---- Idea ----
    create tempArrayInput
    def int Max
    for (int i = 0; i < k ; i++){ 
        int cnt = 0;
        find first 'G' HATE HATE# GAH
        then loop find shorttest 'P' from 'G' in these area ***********[G-i...G...G+i]************* 
            if found, pair and mark these two used 
            cnt++
            if cnt > Max assign new Max value
    }
    return Max
""" 

