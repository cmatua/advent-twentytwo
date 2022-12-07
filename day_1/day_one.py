# Advent of Code - 2022, Day 1: Calorie Counting
# Complete

# Opening input and creating calorie_list
with open('calorie_input_list.txt') as f:
    calorie_list = f.read()

# Bunch'a packs carried by elves separated by two new lines
packs = calorie_list.split("\n\n")

# Sum of calories in each elf's pack
elves = []
for pack in packs:
    elf = sum(eval(item) for item in pack.split('\n'))
    elves.append(elf)

# Most calories to least calories
elves.sort(reverse=True)

# Part I
print("The elf carrying the most calories is carrying", max(elves), "calories.")

# Part II
print("The top three elves carrying the most calories are carrying", sum(elves[:3]), "calories altogether.")