import math
if __name__ == "__main__":
    n = 600851475143
    while(n % 2 == 0):
        n = n / 2
        print(n)
    largest = n
    #why sqrt tho
    for i in range(3, int(math.sqrt(n)), 2):
        while(n % i == 0):
            n /= i
            largest = i

    print(largest)