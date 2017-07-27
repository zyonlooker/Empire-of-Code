def transpose(data):
    num_rows = len(data)
    num_cols = len(data[0])
    matrix = [[0 for row in range(num_rows)] for col in range(num_cols)]
    x = 0
    while x < num_cols:
        y = 0
        while y < num_rows:
            matrix[x][y] = data[y][x]
            y += 1
        x += 1
    return matrix


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert transpose([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]) == [[1, 4, 7],
                                      [2, 5, 8],
                                      [3, 6, 9]], "Square matrix"
    assert transpose([[1, 4, 3],
                      [8, 2, 6],
                      [7, 8, 3],
                      [4, 9, 6],
                      [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                      [4, 2, 8, 9, 8],
                                      [3, 6, 3, 6, 1]], "Rectangle matrix"

    print("Use 'Check' to earn sweet rewards!")

