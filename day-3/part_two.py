def get_o2_rating(data: list) -> int:
    crit_nums = data
    pos = 0
    
    while len(crit_nums) > 1:
        pos_sum_0 = sum(x[pos] == '0' for x in crit_nums)
        pos_sum_1 = len(crit_nums) - pos_sum_0
        
        if pos_sum_0 > pos_sum_1:
            crit_nums = [i for i in crit_nums if i[pos] == '0']
        else:
            crit_nums = [i for i in crit_nums if i[pos] == '1']
                
        pos += 1
    
    o2_rating = int(crit_nums[0], 2)
    
    return o2_rating

def get_co2_rating(data: list) -> int:
    crit_nums = data
    pos = 0
    
    while len(crit_nums) > 1:
        pos_sum_0 = sum(x[pos] == '0' for x in crit_nums)
        pos_sum_1 = len(crit_nums) - pos_sum_0
        
        if pos_sum_0 > pos_sum_1:
            crit_nums = [i for i in crit_nums if i[pos] == '1']
        else:
            crit_nums = [i for i in crit_nums if i[pos] == '0']
                
        pos += 1
    
    co2_rating = int(crit_nums[0], 2)
    
    return co2_rating
    
def main():
    filepath = 'D:\\programming\\aoc-2021\\day-3\data.txt'

    with open(filepath, 'r') as file:
        data = file.read().split('\n')
    
    o2_rating = get_o2_rating(data)
    co2_rating = get_co2_rating(data)
    
    print(f"{o2_rating = }\n{co2_rating = }\n{o2_rating * co2_rating = }")

if __name__ == "__main__":
    main()
