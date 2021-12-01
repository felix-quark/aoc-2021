filepath = 'D:\\programming\\aoc-2021\\day-1\data.txt'

with open(filepath, 'r') as file:
    data = [int(i) for i in file.read().split('\n')]

# zip, my beloved 
count = sum(x < y for x, y in zip(data, data[1:]))

print(count)    
