import functions

file_name: str = "./4/input"
sums: int = 0
sums_2: int = 0

with open(file_name, "r") as file:
    for line in file:
        formated_line = line.rstrip()

        contained = False
        ranges = formated_line.split(",")

        range1 = ranges[0].split("-")
        set1 = set(range(int(range1[0]), int(range1[1]) + 1))
        if (len(set1) == 0):
            set1 = set([int(i) for i in range1])

        range2 = ranges[1].split("-")
        set2 = set(range(int(range2[0]), int(range2[1]) + 1))
        if (len(set2) == 0):
            set2 = set([int(i) for i in range2])

        contained = functions.check_if_sets_contained(set1, set2)

        if contained:
            sums += 1

        disjoint = functions.check_if_sets_are_disjoin(set1, set2)

        if not disjoint:
            sums_2 += 1

print(sums)
print(sums_2)
