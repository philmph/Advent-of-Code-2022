def calorie_counting(file_name: str):
    highest: int = 0
    current: int = 0
    sums: list(int) = []

    with open(file_name, "r") as file:
        for line in file:
            formated_line = line.rstrip()

            # Check if string is empty
            if (not formated_line):
                # Add to list and reset counter
                sums.append(current)
                current = 0
            else:
                current += int(formated_line)

    # Add final calculation
    sums.append(current)

    return max(sums)


print(calorie_counting("./input"))
