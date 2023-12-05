import re

file_path = open('/Users/jonathan/PycharmProjects/adventofcodepuzzles/advent-of-code/day5/fuckingseeds')
strings_list = file_path.readlines()

seed_target = re.findall(r'\b\d+\b', strings_list[0])
seeds = [int(num) for num in seed_target]


seed_to_soil_map = []
seed_to_soil_map_indv = []
for char in strings_list[3:40]:
    seed_to_soil_map_indv = re.findall(r'\d+', char)
    seed_to_soil_map_indv = [int(num) for num in seed_to_soil_map]
    seed_to_soil_map.append(seed_to_soil_map_indv)

for seed in seeds:
    soil_for_currentSeed = 0
    for list in seed_to_soil_map:
        if (list[0] + list[2]) > seed > list[0]:
            soil_for_currentSeed = list[1] + (seed - list[0])
            print(f'For the seed: {seed}, the soil is: {soil_for_currentSeed}')
