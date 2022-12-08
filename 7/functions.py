def tryparse_int(i):
    try:
        output = int(i)
        return output
    except ValueError:
        return 0


def get_folder_info(dir):
    output = 0

    for line in dir:
        if "$" in line:
            break

        size = tryparse_int(line.split()[0])
        output += size

    print("Size is:", output)
    return output
