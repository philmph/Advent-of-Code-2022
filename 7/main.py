import functions as f


def load_inputfile_contents(filepath: str) -> list[str]:
    output: list[str] = []
    with open(filepath, "r") as file:
        for line in file:
            formated_line = line.rstrip()
            output.append(formated_line)

    return output


filecontent = load_inputfile_contents("./7/input")

depth = 0
index = 0
folders = {}

for line in filecontent:
    index += 1

    if "$ cd" in line:
        current_folder = line.split()[-1]

        if current_folder == "..":
            depth -= 1
        else:
            if current_folder == "/":
                depth = 0
            else:
                depth += 1
            folders[current_folder] = {
                "depth": depth,
            }
    elif "$ ls" in line:
        print("Checking folder:", current_folder, "with depth:", depth)
        folders[current_folder]["filesize"] = f.get_folder_info(
            filecontent[index + 1:]
        )

output = 0

for i in folders.values():
    if i["filesize"] < 100000:
        output += i["filesize"]

print(output)
