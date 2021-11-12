import os
import math as m

file_dir = 'input/8.6 extra.txt'

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, file_dir)
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()

global days
global values
days = int(lines[0])
values = [float(v) for v in lines[1].split(" ")]
print(values)


def keng_kumrai_Brute_Force():
    best_buy_day = m.inf
    best_sell_day = m.inf
    best_buy_rate = m.inf
    best_sell_rate = m.inf
    best_profit = 0
    num_of_day = 0

    for i in range(days):
        for j in range(days):
            if j > i:
                profit = values[j] - values[i]
                if profit >= best_profit:
                    best_buy_day = i + 1
                    best_buy_rate = values[i]
                    best_sell_day = j + 1
                    best_sell_rate = values[j]
                    best_profit = profit
                    num_of_day = j - i
                    
    print("Best day to buy : " + str(best_buy_day))
    print("Best value to buy : " + str(best_buy_rate))
    print("Best day to sell : " + str(best_sell_day))
    print("Best value to sell : " + str(best_sell_rate))
    best_profit = "{:.2f}".format(best_profit)
    print("Best profit : " + str(best_profit))
    print("Number of days until sell : " + str(num_of_day))


def keng_kumrai_Divide_And_Conquer(arr: list):
  
    if len(arr) == 0:
        return 0

    def Recursion(arr, lhs, rhs):

        if lhs == rhs:
            return (0, arr[lhs], arr[rhs])

        mid = lhs + (rhs - lhs) // 2

        (leftProfit,  leftMin,  leftMax) = Recursion(arr, lhs, mid)
        (rightProfit, rightMin, rightMax) = Recursion(arr, mid + 1, rhs)

        midProfit = rightMax - leftMin
        maxProfit = max(leftProfit, rightProfit, midProfit)

        return (maxProfit, min(leftMin, rightMin), max(leftMax, rightMax))

    profit, all_min, all_max = Recursion(arr, 0, len(arr) - 1)
    return (profit, all_min, all_max)


def finding_nemoday(all_min, all_max, profit):
    if profit == 0.00:
        return (1, 1)
    buy_day = None
    sell_day = None
    for i in range(days):
        if buy_day == None:
            if values[i] == all_min:
                buy_day = i
        else:
            if values[i] == all_max:
                sell_day = i
    
    return (buy_day + 1, sell_day + 1)


print("----------------------------------------------------------------------------------------")
print("Brute Force method:")
keng_kumrai_Brute_Force()
def extra():
    print("----------------------------------------------------------------------------------------")
    print("Divide and Conquer method:")
    max_profit, all_min, all_max = keng_kumrai_Divide_And_Conquer(values)
    buy_day, sell_day = finding_nemoday(all_min, all_max, max_profit)
    max_profit = "{:.2f}".format(max_profit)
    # print('b_day = ' + str(b_day))
    # print('s_day = ' + str(s_day))
    # print('all_min = ' + str(all_min))
    # print('all_max = ' + str(all_max))
    print("Best day to buy : " + str(buy_day))
    print("Best value to buy : " + str(values[buy_day - 1]))
    print("Best day to sell : " + str(sell_day))
    print("Best value to sell : " + str(values[sell_day - 1]))
    print("Best profit : " + str(max_profit))
    print("Number of days until sell : " + str(sell_day - buy_day))


def combine(left_profit, left_buy_value, left_sell_value, left_max_value, left_min_value, right_profit, right_buy_value, right_sell_value, right_max_value, right_min_value):
    newProfit = right_max_value - left_min_value
    if right_profit >= left_profit:
        if newProfit >= right_profit:
            profit = newProfit
            buy = left_min_value
            sell = right_max_value
        else:
            profit = right_profit
            buy = right_buy_value
            sell = right_sell_value
    else:    
        if newProfit >= left_profit:
            profit = newProfit
            buy = left_min_value
            sell = right_max_value
        else:
            profit = left_profit
            buy = left_buy_value
            sell = left_sell_value
    max_value = max(left_max_value, right_max_value)
    min_value = min(left_min_value, right_min_value)

    return (profit, buy, sell, max_value, min_value)
       

def DIVIDEnCONQUER(left_pivot , right_pivot):
    if (left_pivot == right_pivot):
        return (0, values[left_pivot], values[left_pivot], values[right_pivot], values[right_pivot])

    mid_point = left_pivot + (right_pivot - left_pivot) // 2
    left_profit, left_buy_value, left_sell_value, left_max_value, left_min_value = DIVIDEnCONQUER(left_pivot, mid_point)
    right_profit, right_buy_value, right_sell_value, right_max_value, right_min_value = DIVIDEnCONQUER(mid_point + 1, right_pivot)
    return(combine(left_profit, left_buy_value, left_sell_value, left_max_value, left_min_value, right_profit, right_buy_value, right_sell_value, right_max_value, right_min_value))
        

def altDnQ():
    left_pivot = 0
    right_pivot = len(values)-1
    profit, buy_value, sell_value, max_value, min_value = DIVIDEnCONQUER(left_pivot, right_pivot)
    buy_day = values.index(buy_value)
    sell_day = values.index(sell_value)
    return (profit, buy_day, buy_value, sell_day, sell_value, max_value, min_value)


print("----------------------------------------------------------------------------------------")
print("Altenate Divide and Conquer method:")
profit, buy_day, buy_value, sell_day, sell_value, max_value, min_value = altDnQ()
profit = "{:.2f}".format(profit)
print('Best day to buy : ' + str(buy_day + 1))
print('Best value to buy : ' + str(buy_value))
print('Best day to sell : ' + str(sell_day + 1))
print('Best value to sell : ' + str(sell_value))
print("Best profit : " + str(profit))
print('Number of days until sell : ' + str(sell_day - buy_day))

#           _.-/`)
#          // / / )
#       .=// / / / )
#      //`/ / / / /
#     // /     ` /
#    ||         /
#     \\       /
#      ))    .'
#     //    /
#          /

#           _.-/`)
#          // / / )
#       .=// / / / )
#      //`/ / / / /
#     // /     ` /
#    ||         /
#     \\       /
#      ))    .'
#     //    /
#          /



#           _.-/`)
#          // / / )
#       .=// / / / )
#      //`/ / / / /
#     // /     ` /
#    ||         /
#     \\       /
#      ))    .'
#     //    /
#          /

#           _.-/`)
#          // / / )
#       .=// / / / )
#      //`/ / / / /
#     // /     ` /
#    ||         /
#     \\       /
#      ))    .'
#     //    /
        #  /
