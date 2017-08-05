def golf(n):
    l = [0]
    for i in range(len(n)):
        l += [n[i] + max(l[i], l[i-1])]
    return max(l[-2:])

# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf((5, -3, -1, 2)) == 6
#    assert golf((5, 6, -10, -7, 4)) == 8
#    assert golf((-11, 69, 77, -51, 23, 67, 35, 27, -25, 95)) == 393
#    assert golf((-21, -23, -69, -67, 1, 41, 97, 49, 27)) == 125
#    print("Use 'Check' to earn sweet rewards!")
