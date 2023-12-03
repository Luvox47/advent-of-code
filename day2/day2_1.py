import re

file_path = '/Users/jonathan/PycharmProjects/adventofcodepuzzles/day2/day2_puzzleinput'
with open(file_path, 'r') as file:
    strings_list = [line.strip() for line in file]

id_sum = 0
currentID = 0

for string in strings_list:
    currentID += 1
    print(currentID)
    red_numbers = re.findall(r'(\d+) red', string)
    red_result = all(int(num) <= 12 for num in red_numbers)
    green_numbers = re.findall(r'(\d+) green', string)
    green_result = all(int(num) <= 13 for num in green_numbers)
    blue_numbers = re.findall(r'(\d+) blue', string)
    blue_result = all(int(num) <= 14 for num in blue_numbers)

    if red_result == True and green_result == True and blue_result == True:
        id_sum += currentID
    else:
        print('Not a valid Game')


print(id_sum)