from collections import Counter

file_path = open('/Users/jonathan/PycharmProjects/adventofcodepuzzles/advent-of-code/day4/scratchcards')
strings_list = file_path.readlines()

# The sum of matches in for i in range(matches): newCards[].append(originalCards[currentCard + i + 1])

def extractNumb (line):
    number = ''
    numbers = []
    win = 0
    for i in line:
            if i.isdigit():
                number += i
            else:
                if number:
                    numbers.append(number)
                    number = ''

    c = Counter(numbers)

    for i in c:
        if c[i] == 2:
            win += 1

    return win



for string in strings_list:

    extractNumb(string[9:])