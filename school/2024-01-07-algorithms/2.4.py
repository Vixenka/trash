m = 0
with open('binarne.txt') as file:
    while line := file.readline().strip():
        if len(line) <= 16:
            m = max(m, int(line, 2))

print(m)
