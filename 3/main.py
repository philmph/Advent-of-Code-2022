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
