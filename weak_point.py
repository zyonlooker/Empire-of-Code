def golf(matrix):
    durability_of_rows = []
    durability_of_cols = []
    for row in matrix:
        durability_of_rows.append(sum(row))
    for idx_col in range(len(matrix)):
        durability_of_col = []
        for idx_row in range(len(matrix)):
            item = matrix[idx_row][idx_col]
            durability_of_col.append(item)
        durability_of_cols.append(sum(durability_of_col))
    x = min_find(durability_of_rows)
    y = min_find(durability_of_cols)
    return [x, y]
    
def min_find(durabilities):
    idx = 0
    for n in range(1, len(durabilities)):
        if durabilities[n] < durabilities[idx]:
            idx = n
    return idx

#if __name__ == '__main__':
#  # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf([[7, 2, 7, 2, 8],
#              [2, 9, 4, 1, 7],
#              [3, 8, 6, 2, 4],
#              [2, 5, 2, 9, 1],
#              [6, 6, 5, 4, 5]]) == [3, 3]
#    assert golf([[7, 2, 4, 2, 8],
#              [2, 8, 1, 1, 7],
#              [3, 8, 6, 2, 4],
#              [2, 5, 2, 9, 1],
#              [6, 6, 5, 4, 5]]) == [1, 2]
#    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
