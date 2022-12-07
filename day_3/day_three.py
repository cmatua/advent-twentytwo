# Advent of Code - 2022, Day 3: Rucksack Reorganization
import string

# Opening rucksack contents
with open('rucksack_contents.txt') as f:
    rucksacks = f.read().split("\n")

# Initialize priority sum
priority_sum = 0

# Splitting the rucksack into two compartments
for rucksack in rucksacks:
    compartment_size = int(len(rucksack) / 2)
    first = rucksack[:compartment_size]
    second = rucksack[compartment_size:]

    for i in first:
        # Finding the item contained in both compartments
        if i in second:
            # Adding the item priority to priority sum
            priority_sum += string.ascii_letters.index(i) + 1
            break

# Initializing badge sum
badge_sum = 0

# Counting rucksacks
num_rucksacks = len(rucksacks)

# Grouping the rucksacks in threes
for i in range(0, num_rucksacks - 2, 3):
    rucksack_one = rucksacks[i]
    rucksack_two = rucksacks[i + 1]
    rucksack_three = rucksacks[i + 2]

    for x in rucksack_one:
        # Finding the badge
        if x in rucksack_two and x in rucksack_three:
            badge_sum += string.ascii_letters.index(x) + 1
            break

# part I
print("The sum of the priorities of items in both compartments is:", priority_sum)

# part II
print("The sum of the priorities of items in each badge group is:", badge_sum)
