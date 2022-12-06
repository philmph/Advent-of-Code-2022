def load_inputfile_contents(filepath: str) -> list[str]:
    output: list[str] = []
    with open(filepath, "r") as file:
        for line in file:
            formated_line = line.rstrip()
            output.append(formated_line)

    return output


def find_unique_sequence_of_n(s, n):
    for i in range(0, len(s)):
        if len(set(s[i:i + n])) == n:
            return i


filecontent = load_inputfile_contents("./6/input")

output = find_unique_sequence_of_n(filecontent[0], 4) + 4
print(output)

output = find_unique_sequence_of_n(filecontent[0], 14) + 14
print(output)
