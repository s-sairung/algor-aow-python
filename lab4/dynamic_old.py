'''
from pydantic import validate_arguments

global coins
global cur_change
global all_changes
global solutions
global amount
cur_change = []
all_changes = []


# n | solutions

# list 1 สมาชิกเหมือน list 2 มั้ย
def lists_are_equal(list1, list2):
    temp = list1
    for a in temp:
        for b in list2:
            if a == b:
                temp.remove(a)
    return len(temp) == 0

@validate_arguments
def change(n: int):

    if n < 0:
        if len(cur_change) != 0:
            cur_change.pop()
        return
    if n == 0: 
        temp = cur_change.copy()
        all_changes.append(temp)
        if len(cur_change) != 0:
            cur_change.pop()
        return

    # TODO: เช็คว่า n เคยคิดยัง เอากลับมาใช้
    # if n in ...
    #   temp = ...ของ n
    #   temp
    #   all_changes.append(...)
    # return

    for c in coins:
        cur_change.append(c)
        change(n - c)

    if len(cur_change) != 0:
        cur_change.pop()
    return
    


# tester ja chai ka
coins = {1, 5, 3}
amount = 5
change(amount)
print(all_changes)

arr1 = {[3, 5, 1], [2, 4, 3]} # จำนวนเหรียญแต่ละประเภท
arr2 = {[3, 5, 1], [2, 4, 3]} # 0 = เหรียญมูลค่าน้อยสุด
arr3 = [4, 2]
d = {}
d["ar"] = arr1
print(d["ar"] == arr2)
'''