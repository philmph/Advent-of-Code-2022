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


def find_common_group_badge(rucksack_contents: list[str]) -> str:
    assert len(rucksack_contents) == 3, "rucksack_contents is not equal to 3"
    for item in set(rucksack_contents[0]):
        if (item in rucksack_contents[1]):
            if (item in rucksack_contents[2]):
                return item


def split_list_every_n(l: list[str], n: int) -> list[list[str]]:
    return [l[i:i+n] for i in range(0, len(l), n)]
