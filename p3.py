import math

def is_prime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i = i + 1
    return True

def biggest_prime(n):
    i = int(math.sqrt(n))
    biggest = 1
    while 0 < i:
        if is_prime(i) and n % i == 0:
            return i
        i = i - 1

print(biggest_prime(600851475143))
