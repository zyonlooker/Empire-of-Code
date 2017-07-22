def median(data):
    if len(data) % 2 != 0:
        data.sort()
        median = data[int((len(data) - 1)/2)]
    else:
        data.sort()
        median = 0.5 * (data[int(len(data)/2)] + data[int(len(data)/2) - 1])
    return median

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert median([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert median([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert median([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert median([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert median(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")

    print("Earn cool rewards by using the 'Check' button!")

