def get_folder_size(dir):
    sum = 0

    for line in dir:
        try:
            size = int(line.split()[0])
            print("Adding to sum:", size)
            sum += size
        except ValueError:
            print(line, "is not a file.")

    print("Sum is:", sum)
    return sum
