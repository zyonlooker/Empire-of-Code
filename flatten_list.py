def flat_list(array):
    new_array = []
    def sub_flat_list(array):
        nonlocal new_array
        for item in array:
            if type(item) == list:
                sub_flat_list(item)
            else:
                new_array.append(item)
        return new_array
    sub_flat_list(array)
    return new_array

if __name__ == "__main__":
    assert flat_list([1, 2, 3]) == [1, 2, 3], "Flat"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "One"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Nested"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "In In"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

