import sys
import re
from collections import Counter


file_path = open('/Users/jonathan/PycharmProjects/adventofcodepuzzles/advent-of-code/day4/scratchcards')

strings_list = file_path.readlines()

crackTracker = []

for i in strings_list:
    crackTracker.append(1)


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


for index, string in enumerate(strings_list):
    matchesCard = extractNumb(string[9:])
    i = 1
    while i <= matchesCard:
        if index + i <= len(crackTracker):
            crackTracker[index + i] += 1 * crackTracker[index]
        i += 1


print(crackTracker)
print(sum(crackTracker))
