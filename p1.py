sum = 0
i = 0
while i < 1000:
    if i % 5 == 0 or i % 3 == 0:
        sum = sum + i
    i = i + 1
print(sum)