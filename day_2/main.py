def is_safe(nums):
    for i in range(len(nums)-1):
        a, b = nums[i], nums[i+1]
        if not 1 <= abs(a-b) <= 3:
            return False

        if i == len(nums)-2:
            continue

        c = nums[i+2]

        if not a < b < c and not a > b > c:
            return False

    return True

def part1():
    reports = []
    with open("input.txt") as file:
        reports = file.readlines()

    safe_counter = 0

    for report in reports:
        numbers = list(map(int, report.split(' ')))

        if is_safe(numbers):
            safe_counter += 1

    return safe_counter


def part2():
    reports = []
    with open("input.txt") as file:
        reports = file.readlines()

    safe_counter = 0

    for report in reports:
        numbers = list(map(int, report.split(' ')))

        if is_safe(numbers):
            safe_counter += 1
        else:
            for i in range(len(numbers)):
                if is_safe(numbers[:i]+numbers[i+1:]):
                    safe_counter += 1
                    break

    return safe_counter


if __name__ == "__main__":
    print("Day 2, Part 1: " + str(part1()))
    print("Day 2, Part 2: " + str(part2()))