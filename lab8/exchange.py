import os
import math as m

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/8.2.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()
# print(lines)

global days
global values
days = int(lines[0])
values = [float(v) for v in lines[1].split(" ")]
print("----------------------------input--------------------------------------------------------")
# print(days)
# print(values)


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

    if end == start: # เหลือวันเดียว
        return (0, values[start], values[end], start, end)
        

    divider = end + (start - end)//2
    prof_l, min_l, max_l, buy_l, sell_l = keng_kumrai_Divide_And_Conquer(start, divider)
    prof_r, min_r, max_r, buy_r, sell_r = keng_kumrai_Divide_And_Conquer(divider + 1, end)
    return keng_kumrai_Combine(min_l, max_l, prof_l, min_r, max_r, prof_r, buy_l, sell_l, buy_r, sell_r)


    
def keng_kumrai_Combine(min_l: int, max_l: int, prof_l: int, min_r: int, max_r: int, prof_r: int, buy_l: int, sell_l: int, buy_r: int, sell_r: int):

    # profit = max(prof_l, prof_r, max_r - min_l)
    min_value = None
    max_value = None

    '''
    if A > B and A > C, then print A.
    else if B > A and B > C, then print B.
    else print C.
    '''

    profit = None
    buy_day = None
    sell_day = None

    prof_lr = max_r - min_l
    # prof_l = max_l - min_l
    # prof_r = max_r - min_r

    if prof_r > prof_l and prof_r > prof_lr: # prof_r is max
        buy_day = buy_r
        sell_day = sell_r
        profit = prof_r
    elif prof_l > prof_r and prof_l > prof_lr: # prof_l is max
        buy_day = buy_l
        sell_day = sell_l
        profit = prof_l
    elif prof_lr > prof_r and prof_lr > prof_l: # prof_lr is max
        buy_day = buy_l
        sell_day = sell_r
        profit = prof_lr
    elif prof_r == prof_lr == prof_l: # เท่ากันสามอัน
        # print("prof_r == prof_lr == prof_l")
        buy_day = buy_l
        sell_day = sell_l
        profit = prof_l
    elif prof_r == prof_lr: # ขวาเท่ากับกลาง 
        # print("prof_r == prof_lr")
        buy_day = buy_l
        sell_day = sell_r
        profit = prof_lr
    elif prof_l == prof_lr: # ซ้ายเท่ากับกลาง 
        # print("prof_l == prof_lr")
        buy_day = buy_l
        sell_day = sell_l
        profit = prof_l
    elif prof_r == prof_l: # ซ้ายเท่ากับขวา
        # print("prof_l == prof_r")
        buy_day = buy_l
        sell_day = sell_l
        profit = prof_l
        
        '''
        suuuuuuuuuuuuuuuuu suuuuuuuuuuuuuuuuuuu mwl
        '''
    min_value = values[buy_day]
    max_value = values[sell_day]
    # profit = max(prof_l, prof_r, max_r - min_l)
    return (profit, min_value, max_value, buy_day, sell_day)

    
print("----------------------------------------------------------------------------------------")
print("Brute Force method:")
keng_kumrai_Brute_Force()
print("----------------------------------------------------------------------------------------")
print("Divide and Conquer method:")
max_profit, min_value, max_value, buy_day, sell_day = keng_kumrai_Divide_And_Conquer(0, days - 1)
max_profit = "{:.2f}".format(max_profit)

print("Best day to buy : " + str(buy_day + 1))
print("Best value to buy : " + str(min_value))
print("Best day to sell : " + str(sell_day + 1))
print("Best value to sell : " + str(max_value))
print("Best profit : " + str(max_profit))
print("Number of days until sell : " + str(sell_day - buy_day))
# i hate this problem so muchhhhhhhh