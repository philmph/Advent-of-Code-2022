def move_n_containers_to_other_stack(n: int, stack_from: list[str], stack_to: list[str]):
    for i in range(0, n):
        print("a")

    return None


def build_initial_container_stacks(filecontent: list[str]):
    # split_index is also the max stack height
    split_index = filecontent.index("") - 1
    stack_count = int(filecontent[split_index][-1])

    # Create array with stack_count empty arrays
    output = [[] for i in range(0, int(stack_count))]

    for i in range(0, split_index):
        for j in range(0, stack_count):
            letter = filecontent[i][j * 4 + 1]
            if letter != " ":
                output[j].append(letter)

    [output[i].reverse() for i in range(0, stack_count)]
    return output
