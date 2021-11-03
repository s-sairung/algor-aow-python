import os
import math as m

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/test.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()
# print(lines)

global days
global values
days = int(lines[0])
values = [float(v) for v in lines[1].split(" ")]
print(days)
print(values)


# O(n^2)
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


# T(1) = O(1)
# T(n) = 2T(n / 2) + O(1)
# T(n) = seta(n)

def keng_kumrai_Divide_And_Conquer(start: int, end: int): # start = 0, end = 4, values = [0..4]

    if end == start: # เหลือค่าเดียว
        return (0, values[start], values[end], start, end)

    divider = (end + start)//2
    prof_l, min_l, max_l, start_l, end_l = keng_kumrai_Divide_And_Conquer(start, divider)
    prof_r, min_r, max_r, start_r, end_r = keng_kumrai_Divide_And_Conquer(divider + 1, end)
    return keng_kumrai_Combine(min_l, max_l, prof_l, min_r, max_r, prof_r, start_l, end_l, start_r, end_r)

    
def keng_kumrai_Combine(min_l: int, max_l: int, prof_l: int, min_r: int, max_r: int, prof_r: int, start_l: int, end_l: int, start_r: int, end_r: int):

    profit = max(prof_l, prof_r, max_r - min_l)

    buy_day = None
    sell_day = None
    if profit == prof_l:
        buy_day = values.index(min_l)
        sell_day = values.index(max_l)
    elif profit == prof_r:
        buy_day = values.index(min_r)
        sell_day = values.index(max_r)
    else:
        buy_day = values.index(min_l)
        sell_day = values.index(max_r)
    
    return (profit, min(min_l, min_r), max(max_l, max_r), buy_day + 1, sell_day + 1)

    
print("----------------------------------------------------------------------------------------")
print("Brute Force method:")
keng_kumrai_Brute_Force()
print("----------------------------------------------------------------------------------------")
print("Divide and Conquer method:")
max_profit, min_value, max_value, s, e = keng_kumrai_Divide_And_Conquer(0, days - 1)
max_profit = "{:.2f}".format(max_profit)
print("Best day to buy : " + str(s))
print("Best value to buy : " + str(min_value))
print("Best day to sell : " + str(e))
print("Best value to sell : " + str(max_value))
print("Best profit : " + str(max_profit))
print("Number of days until sell : " + str(e - s))
# i hate this problem so muchhhhhhhhhhhh