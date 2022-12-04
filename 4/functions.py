def check_if_sets_contained(set1: set[int], set2: set[int]) -> bool:
    output = False

    if (set1.issubset(set2)):
        output = True
    elif (set2.issubset(set1)):
        output = True

    print(set1)
    print(set2)
    print(output)

    return output
