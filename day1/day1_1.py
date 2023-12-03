file_path = '/Users/jonathan/PycharmProjects/adventofcode/day1/day1_wordlist.txt'
with open(file_path, 'r') as file:
    strings_list = [line.strip() for line in file]

def intinlist(string):
    numbers = ''
    for i in string:
        if i.isdigit():
            numbers += i

    if len(numbers) > 1:
        two_digit_numb = int(str(numbers[0]) + str(numbers[len(numbers) - 1]))
        return two_digit_numb
    else:
        two_digit_numb = int(str(numbers[0]) + str(numbers[0]))
        return two_digit_numb


finalInt = 0

for string in strings_list:
    finalInt += intinlist(string)


print(finalInt)
