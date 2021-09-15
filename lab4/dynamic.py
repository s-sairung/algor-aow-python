from pydantic import validate_arguments

global coins
global table_ways # dict ที่จะเก็บ ways ที่เราคำนวณเสร็จ
global table_min
coins = [1, 2, 3]
table_ways = {}
table_min = {}

@validate_arguments
def ways(k: int, a: int): 
# k คือ indexเหรียญ(0,1,2)
# a คือ amount ที่เหลือ
# d คือ coins[k]

    if (a, k) in table_ways:
        return table_ways[(a, k)]

    d = coins[k]
    if a == 0:
        table_ways[(0, k)] = 1
        return 1
    if k == 0:
        if a % d == 0:
            table_ways[(a, 0)] = 1
            return 1
        else:
            table_ways[(a, 0)] = 0
            return 0

    if d > a:
        w = ways(k - 1, a)
        table_ways[(a, k)] = w
        return w
    else:
        w = ways(k - 1, a) + ways(k, a - d)
        table_ways[(a, k)] = w
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

@validate_arguments
def min_coin(k: int, a: int):
    pass

print(ways(len(coins) - 1, 5))
print(table_ways)

