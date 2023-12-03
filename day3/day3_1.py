import re

file_path = '/Users/jonathan/PycharmProjects/adventofcodepuzzles/day3/engineschematic'

with open(file_path, 'r') as file:
    strings_list = [line.strip() for line in file]

specialChar = '.0123456789'
numbers = '0123456789'


def findSym ():
    totalSym = 0

    # to the right:
    if posinstr < 139:
        if (string[posinstr - 1]) not in specialChar:
            totalSym += 1
            print(f'symbol left found in: {string[posinstr + 1]}')

    # to the left:
    if posinstr > 0 and posinstr < 139:
        if (string[posinstr + 1]) not in specialChar:
            totalSym += 1
            print(f'symbol right found in: {string[posinstr - 1]}')

    # above:
    string_above = strings_list[currentstr - 1]
    if string_above[posinstr] not in specialChar:
        print(f'symbol above found in {currentstr} position: {posinstr}')
        totalSym += 1

    # below:
    if currentstr < 139:
        string_below = strings_list[currentstr + 1]
        if string_below[posinstr] not in specialChar:
            print(f'symbol below found in {currentstr} position: {posinstr}')
            totalSym += 1

    # diagonal:
    if currentstr > 0:
        if posinstr > 0:
            string_diagonal_up_left = strings_list[currentstr - 1]
            if string_diagonal_up_left[posinstr - 1] not in specialChar:
                print(f'symbol diagonal left up found in {currentstr} position: {posinstr}')
                totalSym += 1
        if posinstr < 139:
            string_diagonal_up_right = strings_list[currentstr - 1]
            if string_diagonal_up_right[posinstr + 1] not in specialChar:
                print(f'symbol diagonal right up found in {currentstr} position: {posinstr}')
                totalSym += 1
    if currentstr < 139:
        if posinstr > 0:
            string_diagonal_down_left = strings_list[currentstr + 1]
            if string_diagonal_down_left[posinstr - 1] not in specialChar:
                print(f'symbol diagonal left down found in {currentstr} position: {posinstr}')
                totalSym += 1
        if posinstr < 139:
            string_diagonal_down_right = strings_list[currentstr + 1]
            if string_diagonal_down_right[posinstr + 1] not in specialChar:
                print(f'symbol diagonal right down found in {currentstr} position: {posinstr}')
                totalSym += 1

    return totalSym

currentstr = -1
finalSum = 0
currentTot = 0

for string in strings_list:
    currentstr += 1
    posinstr = -1
    currentNumber = ''

    for i in string:
        posinstr += 1

        if i.isdigit():
            currentNumber += str(i)
            print(f'current Number in isDigit {currentNumber}')
            currentTot += findSym()

        if posinstr < 139:
            if string[posinstr + 1] not in numbers and currentTot < 1:
                currentNumber = ''
            if string[posinstr + 1] not in numbers and currentTot > 0:
                finalSum += int(currentNumber)
                print(finalSum)
                currentNumber = ''
                currentTot = 0
        if posinstr == 139:
            if currentTot > 0:
                finalSum += int(currentNumber)
                currentNumber = ''

print(finalSum)