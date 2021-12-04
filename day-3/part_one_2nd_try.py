def gamma_epsilon(cols: list) -> tuple:
    l = len(cols[0]) / 2
    gamma = ''.join('1' if sum(col) > l else '0' for col in cols)
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
    
    return (int(gamma, 2), int(epsilon, 2))
    
    
def main():
    filepath = 'D:\\programming\\aoc-2021\\day-3\\data.txt'
    
    with open(filepath, 'r') as file:
        cols = list(zip(*[[int(i) for i in line.strip()] for line in file]))
        
    gamma, epsilon = gamma_epsilon(cols)
                
    print(f"{gamma = }\n{epsilon = }\n{gamma * epsilon = }")
        

if __name__ == "__main__":
    main()
