def count_inversion(sequence):
    seq_list = list(sequence)
    count = 0
    for idx in range(len(seq_list)-1, 0, -1):
        idx_down = idx - 1
        while idx_down >= 0:
            if seq_list[idx] < seq_list[idx_down]:
                count += 1
                idx_down -= 1
            else:
                idx_down -= 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

