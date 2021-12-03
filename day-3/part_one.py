def get_gamma_epsilon(data: list) -> tuple:
    gamma = epsilon = ''
    
    for i in range(len(data[0])):
        pos_sum_0 = sum(x[i] == '0' for x in data)
        pos_sum_1 = len(data) - pos_sum_0
        
        if pos_sum_1 > pos_sum_0:
            gamma = gamma + '1'
        elif pos_sum_0 > pos_sum_1:
            gamma = gamma + '0'
        else:
            raise ValueError("Most common bit does not exist.")
        
    for i in gamma:
        if i == '1':
            epsilon = epsilon + '0'
        else:
            epsilon = epsilon + '1'
            
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
            
    return (gamma, epsilon)

def main():
    filepath = 'D:\\programming\\aoc-2021\\day-3\data.txt'

    with open(filepath, 'r') as file:
        data = file.read().split('\n')
        
    gamma, epsilon = get_gamma_epsilon(data)    
        
    print(f"{gamma = }\n{epsilon = }\n{gamma * epsilon = }") 


if __name__ == "__main__":
    main()
