filepath = 'D:\\programming\\aoc-2021\\day-2\data.txt'

with open(filepath, 'r') as file:
    data = [i.split(' ') for i in file.read().split('\n')]
    
x, y, aim = 0, 0, 0    
    
for i in data:
    match i[0]:
        case 'forward':
            x += int(i[1])
            y += aim * int(i[1])
        case 'down':
            aim += int(i[1])
        case 'up':
            aim -= int(i[1])

print(f"{x = }\n{y = }\n{x * y = }")    
   