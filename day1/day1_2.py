file_path = '/Users/jonathan/PycharmProjects/adventofcodepuzzles/day1/day1_wordlist'
with open(file_path, 'r') as file:
    strings_list = [line.strip() for line in file]


finalInt = 0
for string in strings_list:
    new_string = string
    new_string = new_string.replace("one", "1").replace("two", "2").replace("three", "3")
    new_string = new_string.replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7")
    new_string = new_string.replace("eight", "8").replace("nine", "9")
    print(string)
    print(new_string)

    numbers = ''
    for i in new_string:
        if i.isdigit():
            numbers += i

    if len(numbers) > 1:
        two_digit_numb = int(str(numbers[0]) + str(numbers[- 1]))
        print(f'The two digit number for {numbers} is {two_digit_numb}')
    else:
        two_digit_numb = int(str(numbers[0]) + str(numbers[0]))

    finalInt += two_digit_numb


print(finalInt)



