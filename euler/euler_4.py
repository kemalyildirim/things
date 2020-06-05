UP = 999999

def isPalid(num):
    arr = []
    sm = list(str(num))
    smcpy = sm.copy()
    for i in range(0, len(sm)):
        popped = sm.pop()
        arr.insert(i, popped)
    if arr == smcpy :
        return True
    else:
        return False
for i in range (UP, 100000, -1):
    if isPalid(i):
        print(i)