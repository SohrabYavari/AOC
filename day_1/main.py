
def part1():
    lines = []

    with open("input.txt") as file:
        lines = file.readlines()
    
    first_list = []
    second_list = []

    for i in range(len(lines)):
        first_list.append(int(lines[i].split(' ')[0]))
        second_list.append(int(lines[i].split(' ')[-1]))

    first_list.sort()
    second_list.sort()

    total = 0

    for i in range(len(first_list)):
        total += abs(first_list[i] - second_list[i])

    print(total)

part1()