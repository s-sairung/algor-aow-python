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
    '''
    tempArr = arr.copy()
    for i in range(k):
        cnt = 0
        for j in range(len(tempArr)):
            if tempArr[j] == "G":
                if j-i < 0 and tempArr[j-i] == "P":
                    cnt += 1 
    '''
         
"""
 ---- Idea ----
    create tempArrayInput
    def int Max
    for (int i = 0; i < k ; i++){ 
        int cnt = 0;
        find first 'G'
        then loop find shorttest 'P' from 'G' in these area ***********[G-i...G...G+i]************* 
            if found, pair and mark these two used 
            cnt++
            if cnt > Max assign new Max value
    }
    return Max
""" 

