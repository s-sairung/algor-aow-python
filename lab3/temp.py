"""
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
    index_taken = []
    for j in range(len(arr)):
        if arr[j] == "G":
            if arr[j-i] == "P" and (j-i) not in index_taken:
                index_taken.append(j-i)
                index_taken.append
                cnt += 1
            if arr[j+i] == "P" and (j+i) not in index_taken:
                index_taken.append(j+i)
                cnt += 1
            
                





for i in range(len(ar)):
    j = k + ar[i]
"""

# [/P/, /G/, \P\, P, \G\, |G|, |P|, P]; k = 2

# ar = [-1, 1, -2, 2]
# for n in ar
#   index = k + n
#   arr[index]

# class bruteForce:

#     # Reading input file
#     """
#     file = open("/input/Example/3.1.1.txt", "r")
#     string = file.readline()
#     integer = file.readline()
#     file.close()
#     """

#     #Simulate input
#     string = "GGPPGGGGPPPG"
#     integer = "3"

#     # Processing the input
#     global arr
#     arr = []
#     for alphabet in string:
#         arr.append(alphabet)
#     global k
#     k = int(integer)
#     global max_pickup
#     max_pickup = 0
#     global used_index
#     used_index = []
#     global cnt
#     cnt = 0
#     k_ar = [-1, 1, -2, 2]

#     # Pick up passenger in unit range
#     def pick_up(index):
#         cnt_pick = 0
#         if index >= 0 and arr[index] == "P" and index not in used_index:
#             used_index.append(index)
#             cnt_pick += 1
#         return cnt_pick

#     # Pairing Grab and Passenger
#     for i in range(len(arr)):
#         index = k + n
#         if arr[i] == "G":
#             for n in k_ar:
#                 cnt += pick_up(index) #dont miss me somuch ><
#         used_index = []
#         if cnt > max_pickup: 
#             max_pickup = int(cnt) 
#             cnt = 0
                
#     print("Output : " + str(max_pickup) + ".")

"""
    # Pick up passenger in unit range
    def pick_up(index, unit):
        cnt_pick = 0
        p_index_left = index - unit
        p_index_right = index + unit
        if p_index_left >= 0 and arr[p_index_left] == "P" and p_index_left not in used_index:
            used_index.append(p_index_left)
            cnt_pick += 1
        elif p_index_right < len(arr) and arr[p_index_right] == "P" and p_index_right not in used_index:
            used_index.append(p_index_right)
            cnt_pick += 1
        return cnt_pick

    # Pairing Grab and Passenger
    for i in range(len(arr)):
        for j in range(k+1): # ar = [-1, 1, -2, 2]
            if arr[i] == "G":
                cnt += pick_up(i,j)
        used_index = []
        if cnt > max_pickup:
            max_pickup = int(cnt)
            cnt = 0
"""