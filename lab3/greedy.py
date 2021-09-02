def greedy(arr, k):

    print("Input : arr [] = " + str(arr) + ",\n\t\tk = " + str(k) + ".")

    index_taken = []
    max_passenger = 0

    for i in range(len(arr)):
        if arr[i] == 'G':
            start = i - k
            end = i + k
            for j in range(start, end+1):
                if j >= 0 and j < len(arr) and arr[j] == 'P' and j not in index_taken:
                    index_taken.append(j)
                    max_passenger += 1
                    break

    print("Output : " + str(max_passenger) + ".")