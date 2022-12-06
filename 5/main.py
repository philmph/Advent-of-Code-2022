import functions as f


def load_inputfile_contents(filepath: str) -> list[str]:
    output: list[str] = []
    with open(filepath, "r") as file:
        for line in file:
            formated_line = line.rstrip()
            output.append(formated_line)

    return output


filecontent = load_inputfile_contents("./5/input")
split_index = filecontent.index("") - 1

container_stacks = f.build_initial_container_stacks(filecontent)
for line in filecontent[split_index + 2:]:
    commands = line.split()

    for j in range(0, int(commands[1])):
        container_stacks = f.move_container_to_other_stack(
            container_stacks,
            int(commands[3]),
            int(commands[5]))

[print(obj[-1]) for obj in container_stacks]

# Solution to move a max of 3 containers
container_stacks = f.build_initial_container_stacks(filecontent)
for line in filecontent[split_index + 2:]:
    commands = line.split()
    move_counter = int(commands[1])
    loop_count = move_counter // 3 + 1

    for j in range(0, loop_count):
        n = move_counter if move_counter <= 3 else 3
        move_counter -= n

        container_stacks = f.move_n_containers_to_other_stack(
            container_stacks,
            int(commands[3]),
            int(commands[5]),
            n)

print("Part 2")
[print(obj) for obj in container_stacks]


# Final solution
container_stacks = f.build_initial_container_stacks(filecontent)
for line in filecontent[split_index + 2:]:
    commands = line.split()

    container_stacks = f.move_n_containers_to_other_stack(
        container_stacks,
        int(commands[3]),
        int(commands[5]),
        int(commands[1]))

print("Part 3")
print("".join([obj[-1] for obj in container_stacks]))
