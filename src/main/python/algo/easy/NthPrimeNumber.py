import math


def nth_prime(n):
    if n == 0: return 0
    start = 2
    count = 0
    while True:
        if is_prime(start):
            count += 1
            if count == n:
                return start
        start += 1


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for i in range(5):
    print(nth_prime(i), end="\t")
