def golf(n,m=1):
    for d in str(n):m*=int(d)if int(d)else 1
    return m

# How to use lambda efficently in this task?

# a complicated version of using lambda below

# from functools import reduce
# def golf(number):
#     s = list(str(number).replace("0", ""))
#     return reduce(lambda x, y: x * y, map(int, s))


#
# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf(123405) == 120
#    assert golf(999) == 729
#    assert golf(1000) == 1
#    assert golf(1111) == 1
#    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
