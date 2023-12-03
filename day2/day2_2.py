import re

file_path = '/Users/jonathan/PycharmProjects/adventofcodepuzzles/day2/day2_puzzleinput'

with open(file_path, 'r') as file:
    strings_list = [line.strip() for line in file]


finalSum = 0

for string in strings_list:
    #red
    red_list = re.findall(r'(\d+) red', string)
    red_list = [int(num) for num in red_list]
    red_list.sort()
    sorted_red_list = [str(num) for num in red_list]
    red_highest = sorted_red_list[-1]
    print(f'Red Highest: {red_highest}, in List: {sorted_red_list}')

    #green
    green_list = re.findall(r'(\d+) green', string)
    green_list = [int(num) for num in green_list]
    green_list.sort()
    sorted_green_list = [str(num) for num in green_list]
    green_highest = sorted_green_list[-1]
    print(f'Green Highest: {green_highest}, in List: {sorted_green_list}')

    #blue
    blue_list = re.findall(r'(\d+) blue', string)
    blue_list = [int(num) for num in blue_list]
    blue_list.sort()
    sorted_blue_list = [str(num) for num in blue_list]
    blue_highest = sorted_blue_list[-1]
    print(f'Blue Highest: {blue_highest}, in List: {sorted_blue_list}')

    #finalSum
    finalSum += (int(red_highest) * int(green_highest) * int(blue_highest))


print(finalSum)