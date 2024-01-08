import czesc1;

count = 0
with open('binarne.txt') as file:
    while line := file.readline().strip():
        sum = 0
        for digit in line:
            sum += int(digit)

        if czesc1.is_prime(sum):
            count += 1

print(count)
