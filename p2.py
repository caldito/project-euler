a = 1
b = 2
sum = 2
while b < 4000000:
    aux = b
    b = a + b
    a = aux
    if b % 2 == 0:
        sum = sum + b
print(sum)
