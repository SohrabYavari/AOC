import re 

def part1():
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
    
    total = 0
    
    for line in lines: 
        instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        
        for instruction in instructions:
            numbers = list(map(int, re.findall(r"\d+", instruction)))    
            total += numbers[0] * numbers[1]
    
    return total

def part2():
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        
        total = 0 
        
        can_do = True
        
        for line in lines: 
            instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", line)


            for instruction in instructions:
                if instruction == "do()":
                    can_do = True
                    continue
                
                if instruction == "don't()":
                    can_do = False
                    continue
                
                if can_do:
                    numbers = list(map(int, re.findall(r"\d+", instruction)))    
                    total += numbers[0] * numbers[1]
    
    return total
    

if __name__ == "__main__":
    print("Part 1: " + str(part1()))
    print("Part 2: " + str(part2()))