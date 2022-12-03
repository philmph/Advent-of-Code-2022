def get_priority(letter: str) -> int:
    letters: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Index works like arrays, pos 1 = index 0, add 1 to calc
    output: int = letters.index(letter) + 1
    return output
