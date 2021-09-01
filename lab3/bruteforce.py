class bruteForce:

    # Reading input file
    file = open("/input/Example/3.1.1.txt", "r")
    string = file.readline()
    k = file.readline()
    file.close()

    # Processing the input
    arr = []
    for alphabet in string:
        arr.append(alphabet)
    k = int(k)
    global max

    # Pairing Grab and Passenger
    for i in range(k):
        cnt = 0
        for j in range(len(arr)):
            
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

