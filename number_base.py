def convert(str_number, radix):
    table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8":8,\
             "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,\
             "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22,\
             "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,\
             "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35}
    converted = 0
    positions = len(str_number) - 1
    if table[str_number[positions]] >= radix:
        return -1
    else:
        for num in str_number:
            if table[num] > radix:
                return -1
            else:
                converted = converted + radix ** positions * table[num]
                positions -= 1
        return converted


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert("AF", 16) == 175, "Hex"
    assert convert("101", 2) == 5, "Bin"
    assert convert("101", 5) == 26, "5 base"
    assert convert("Z", 36) == 35, "Z base"
    assert convert("AB", 10) == -1, "B > A > 10"

    print("Use 'Check' to earn sweet rewards!")

