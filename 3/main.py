import functions

file_name: str = "./input"
sums: list[int] = []

with open(file_name, "r") as file:
    for line in file:
        formated_line = line.rstrip()
        letter = functions.find_common_compartment_item(formated_line)
        priority = functions.get_priority(letter)
        sums.append(priority)

print(sum(sums))

# Part 2

file_name: str = "./input"

sums: list[int] = []

with open(file_name, "r") as file:
    lines = [line.rstrip() for line in file.readlines()]
    grouped_lines = functions.split_list_every_n(lines, 3)
    for group in grouped_lines:
        letter = functions.find_common_group_badge(group)
        priority = functions.get_priority(letter)
        sums.append(priority)

print(sums)
print(sum(sums))
