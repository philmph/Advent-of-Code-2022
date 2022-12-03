def get_priority(letter: str) -> int:
    letters: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Index works like arrays, pos 1 = index 0, add 1 to calc
    output: int = letters.index(letter) + 1
    return output


def find_common_compartment_item(rucksack_content: str) -> str:
    rucksack_content_length_half: int = len(rucksack_content) // 2

    compartment_1 = set(rucksack_content[:rucksack_content_length_half])
    compartment_2 = rucksack_content[rucksack_content_length_half:]

    for item in compartment_1:
        if (item in compartment_2):
            return item
