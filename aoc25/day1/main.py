x = open("input.txt").readlines()
xi = []

for i in x: 
    a = i.replace("\n", "")
    directions = a[0]
    amount = int(a[1:])
    new_dict = {'dir': directions, 'num': amount}
    xi.append(new_dict)

def part1(data= xi, start: int = 50,  zeros: int = 0):
        
    for i in data: 
        if i['dir'] == 'L':
            start = start - i['num']
        else: 
            start = start + i['num']
        
        start = start % 100  
        
        if start == 0:
            zeros += 1
    
    return zeros

print('Zeros:', part1())

def part2(data = xi, start: int = 50): 
    curr_pos = start
    zero_counter = 0
    
    for i in data:
        clicks = i['num']
        
        for _ in range(clicks):
            if i['dir'] == 'R':
                curr_pos = (curr_pos + 1) % 100
            else: 
                curr_pos = (curr_pos - 1) % 100
            
            if curr_pos == 0:
                zero_counter += 1
            
            
    return zero_counter


print('password method: ', part2())
    