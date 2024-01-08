count = 0
with open('binarne.txt') as file:
    while line := file.readline().strip():
        if len(line) / 8 != 1:
            continue
        
        if line[:4] == line[4:]:
            count += 1

print(count)
