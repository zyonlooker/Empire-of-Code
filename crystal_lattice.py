def golf(c):
    z = 0
    while z < len(c) - 1:
        x = 0
        while x < len(c[0]) - 1:
            y = 0
            while y < len(c[0][0]) - 1:
                if c[z][x][y] == c[z][x][y+1]\
                        or c[z][x][y] == c[z][x+1][y]\
                        or c[z][x][y] == c[z+1][x][y]:
                    return 0
                y += 1
            x += 1
        z += 1
    return 1

# if __name__ == "__main__":
#    assert golf([[["X", "Z"],
#                   ["Z", "X"]],
#                  [["Z", "X"],
#                   ["X", "Z"]]]) == True, "1st example"
#    assert golf([[["X", "Z"],
#                   ["Z", "X"]],
#                  [["X", "Z"],
#                   ["Z", "X"]]]) == False, "2nd example"
#    print("All done? Earn rewards by using the 'Check' button!")

