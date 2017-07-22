def check_line(line):
    length = len(line)
    line_prime = line[1:]
    for idx in range(length-1):
        if line_prime[idx] == line[idx]:
            return False
    if line[length-1] == line[length-2]:
        return False
    else:
        return True

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_line(["X", "Z", "X"]) == True
    assert check_line(["X", "Z", "X", "X"]) == False
    assert check_line(["X", "Z"]) == True
    assert check_line(["Z", "X"]) == True
    assert check_line(["Z", "X", "Z", "X", "Z", "Z", "X"]) == False

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

