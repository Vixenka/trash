def bcd_to_int(code):
    pow = 8
    n = 0
    for digit in code:
        n += pow * int(digit)
        pow //= 2
    
    if n > 9:
        return None
    return n

count = 0
with open('binarne.txt') as file:
    while line := file.readline().strip():
        for i in range(0, len(line) // 4):
            j = i * 4
            if bcd_to_int(line[j:j+4]) is None:
                count += 1

print(count)
