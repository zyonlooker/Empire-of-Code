def is_skew_symmetric(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix):
            if matrix[i][j] != -matrix[j][i]:
                return False
            j += 1
        i += 1
    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_skew_symmetric([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]), "1st example"
    assert not is_skew_symmetric([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]), "2nd example"
    assert not is_skew_symmetric([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]), "3rd example"

    print("All set? Click 'Check' to review your code and earn rewards!")

