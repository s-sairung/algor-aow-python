from pydantic import validate_arguments
import os

global coins
global table_ways # dict ที่จะเก็บ ways ที่เราคำนวณเสร็จ
global table_min
table_ways = {}
table_min = {}


@validate_arguments
def ways(k: int, a: int): 
# k คือ indexเหรียญ(0,1,2)
# a คือ amount ที่เหลือ
# d คือ coins[k]

    if (k, a) in table_ways:
        return table_ways[(k, a)]

    d = coins[k]
    if a == 0:
        table_ways[(k, 0)] = 1
        return 1
    if k == 0:
        if a % d == 0:
            table_ways[(0, a)] = 1
            return 1
        else:
            table_ways[(0, a)] = 0
            return 0

    if d > a:
        w = ways(k - 1, a)
        table_ways[(k, a)] = w
        return w
    else:
        w = ways(k - 1, a) + ways(k, a - d)
        table_ways[(k, a)] = w
        return w



# Tester
# ส่ง ways(len(coins),)

'''
กลับมาเร็วทางบ้านให้อภัยแล้ว นุยังไม่พร้อม รอก่อนนะพ่อ 
ท่ดๆ  มือลั่น 
มาเร็วช่วยกันทำ
plzzz  เกือบไปได้แล้วสสสสวววว แปปนุงใงๆกๆๆ้โอกาสนุ ครับท่านสมาชิก 
5555555555555555555555555555555555555

!!! สมการหน้า 7 ขาดไปนิดนึง แต่ทำอันนั้นไปก่อนได้ 
อันนั้นคืออะไรวะ แบบ ให้แถวบนสุด = 1 or some shit oh my ทำ recursive ให้เสร็จก่อนละกัน

'''
global cnt_coins_arr
@validate_arguments
def min_coin(k: int, a: int):

    if (k, a) in table_min:
        return table_min[(k, a)]

    d = coins[k]
    if a == 0:
        table_min[(k, 0)] = 0
        return 0
    if k == 0:
        init = a / d
        table_min[(0, a)] = init
        return init

    if d > a:
        n = min_coin(k - 1, a)
        table_min[(k, a)] = n
        return n
    else:
        n = min(min_coin(k - 1, a), min_coin(k, a - d) + 1)
        table_min[(k, a)] = n
        return n


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/4.3.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()

amount = lines[0]
coins = [int(c.strip()) for c in lines[1].split(' ')]
coins.sort()

# coins = [1, 2, 3]
# amount = 5
k = len(coins) - 1

print('Amount = ' + str(amount))
print('coins[] = ' + str(coins))
print('Way(s) to make change = ' + str(ways(k, amount)))
print('Minimum of Coin(s) is = ' + str(min_coin(k, amount)))

