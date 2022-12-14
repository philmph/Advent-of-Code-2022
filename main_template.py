import functions as f


def load_inputfile_contents(filepath: str) -> list[str]:
    output: list[str] = []
    with open(filepath, "r") as file:
        for line in file:
            formated_line = line.rstrip()
            output.append(formated_line)

    return output


filecontent = load_inputfile_contents("./FOLDER/input")
print(filecontent)
