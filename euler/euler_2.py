def fib(a, b):
    count = 0
    a, b = b, a+b
    return a,b

limit = 4000000
a,b = 1,1
summ = 0
print(b)
while b < limit:
    if(b % 2 == 0):
        summ += b
    a,b = fib(a,b)
print(summ)