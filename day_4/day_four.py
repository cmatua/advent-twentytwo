# Advent of Code - 2022, Day 4: Camp Cleanup

# Opening cleaning assignments
with open('section_assignments.txt') as f:
    assignments = f.read().split("\n")

# Initializing fully contained assignments
fully_contained_assignments = 0

# Initializing overlapping assignments
overlapping_assignments = 0

for assignment in assignments:
    # Comparing assignments
    pair = assignment.split(",")
    elf_one = pair[0]
    elf_two = pair[1]

    eo_min = eval(elf_one.split("-")[0])
    eo_max = eval(elf_one.split("-")[1])
    et_min = eval(elf_two.split("-")[0])
    et_max = eval(elf_two.split("-")[1])

    # Adding another fully contained assignment if the conditions are met
    if (eo_min <= et_min and eo_max >= et_max) or (eo_min >= et_min and eo_max <= et_max):
        fully_contained_assignments += 1
    
    # Adding another overlapping pair if conditions are met
    for section in range(eo_min, eo_max + 1):
        if section in range(et_min, et_max + 1):
            overlapping_assignments += 1
            break


# part I
print("There are",fully_contained_assignments,"pairs where one range fully contains the other.")

# part II
print("There are",overlapping_assignments,"pairs where the ranges overlap.")

