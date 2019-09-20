def is_palindrome(a):
    s = str(a)
    i = 0
    while i <= len(s)/2:
        if s[i] != s[len(s)-1-i]:
            return False
        i = i + 1
    return True

i = 100
j = 100
biggest = 0
while i < 1000:
    while j < 1000:
        if is_palindrome(int(i*j)):
            print(is_palindrome(i*j))
            biggest = i*j
        j = j + 1
    i = i + 1
print(biggest)
