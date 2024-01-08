import czesc1

count = 0
with open('binarne.txt') as file:
    while line := file.readline().strip():
        n = int(line, 2)
        if n % 4 == 0 and czesc1.is_palindrome(line):
            count += 1

print(count)
