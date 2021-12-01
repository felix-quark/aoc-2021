filepath = 'D:\\programming\\aoc-2021\\day-1\data.txt'

with open(filepath, 'r') as file:
    data = [int(i) for i in file.read().split('\n')]

# in a+b+c and b+c+d, b+c are the same, so just compare a to d
count = sum(x < y for x, y in zip(data, data[3:]))

print(count)    
