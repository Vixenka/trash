count = 0
with open('binarne.txt') as file:
    while line := file.readline().strip():
        half_len = len(line) // 2
        if line[:half_len] == line[half_len:]:
            count += 1

print(count)
