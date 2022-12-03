def play_rps_round(opponent: str, own: str) -> int:
    output: int = 0
    result: str

    match own.upper():
        # Rock
        case "X":
            output += 1
            match opponent.upper():
                case "A":
                    # vs Rock
                    result = "draw"
                case "B":
                    # vs Paper
                    result = "loss"
                case "C":
                    # vs Scissors
                    result = "win"

        # Paper
        case "Y":
            output += 2
            match opponent.upper():
                case "A":
                    # vs Rock
                    result = "win"
                case "B":
                    # vs Paper
                    result = "draw"
                case "C":
                    # vs Scissors
                    result = "loss"

        # Scissors
        case "Z":
            output += 3
            match opponent.upper():
                case "A":
                    # vs Rock
                    result = "loss"
                case "B":
                    # vs Paper
                    result = "win"
                case "C":
                    # vs Scissors
                    result = "draw"

    match result:
        case "win":
            output += 6
        case "draw":
            output += 3

    return output


# Execution part
file_name: str = "./input"
sums: list[int] = []

with open(file_name, "r") as file:
    for line in file:
        formated_line = line.rstrip()
        own, opponent = formated_line.split()
        sums.append(play_rps_round(own, opponent))

print(sum(sums))
