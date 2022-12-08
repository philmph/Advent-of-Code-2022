import functions as f


def load_inputfile_contents(filepath: str) -> list[str]:
    output: list[str] = []
    with open(filepath, "r") as file:
        for line in file:
            formated_line = line.rstrip()
            output.append(formated_line)

    return output


filecontent = load_inputfile_contents("./7/input")
filecontent = list(filter("$ cd ..".__ne__, filecontent))

index = 0
index_start = 0
folder_name = "/"

folder_sizes = {}

for line in filecontent:
    if "$ cd" in line:
        index_end = index

        folder_size = f.get_folder_size(filecontent[index_start:index_end])
        folder_sizes[folder_name] = folder_size

        # Set new index and folder_name after calculating the folder size
        index_start = index + 2
        folder_name = line.split()[-1]
    index += 1

result = sum([i for i in folder_sizes.values() if i < 100000])

print(folder_sizes)
print(result)
