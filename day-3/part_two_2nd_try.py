def life_support_rating(rows: list, n: int) -> int:
    pos = 0
    
    while len(rows) > 1:
        # actually checking for the same condition each time
        # just need to switch what bit val we keep for
        a = n if sum(list(zip(*rows))[pos]) >= len(rows) / 2 else (n + 1) % 2
        rows = [i for i in rows if i[pos] == a]
        
        pos += 1
    
    rating = int(''.join(str(i) for i in rows[0]), 2)
    
    return rating

def main():
    filepath = 'D:\\programming\\aoc-2021\\day-3\\data.txt' 
    
    with open(filepath) as file:
        rows = [[int(i) for i in line.strip()] for line in file]
    
    o2_rating = life_support_rating(rows, 1)
    co2_rating = life_support_rating(rows, 0)
    
    print(f"{o2_rating = }\n{co2_rating = }\n{o2_rating * co2_rating = }")   


if __name__ == "__main__":
    main()
