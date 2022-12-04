def check_if_sets_contained(set1: set[int], set2: set[int]) -> bool:
    output = False

    if (set1.issubset(set2)):
        output = True
    elif (set2.issubset(set1)):
        output = True

    return output


def check_if_sets_are_disjoin(set1: set[int], set2: set[int]) -> bool:
    output = True

    if (not set1.isdisjoint(set2)):
        output = False
    elif (not set2.isdisjoint(set1)):
        output = False

    return output
