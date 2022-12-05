import functions as f


def load_inputfile_contents(filepath: str) -> list[str]:
    output: list[str] = []
    with open(filepath, "r") as file:
        for line in file:
            formated_line = line.rstrip()
            output.append(formated_line)

    return output


filecontent = load_inputfile_contents("./5/input")
container_stacks = f.build_initial_container_stacks(filecontent)

split_index = filecontent.index("") - 1

for line in filecontent[split_index + 2:]:
    commands = line.split()

    for j in range(0, int(commands[1])):
        container_stacks = f.move_container_to_other_stack(
            container_stacks,
            int(commands[3]),
            int(commands[5]))

# print(container_stacks)
[print(obj[-1]) for obj in container_stacks]
# print(result)
