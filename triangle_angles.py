import math
def angles(a, b, c):
    if a + b <= c or a + c <= b or b + c <=a:
        return [0, 0, 0]
    else:
        angle_a_r = math.acos((b**2 + c**2 - a**2)/(2*b*c))
        angle_b_r = math.acos((a**2 + c**2 - b**2)/(2*a*c))
        angle_c_r = math.acos((a**2 + b**2 - c**2)/(2*a*b))
        angle_a = round(angle_a_r * 180 / 3.14159)
        angle_b = round(angle_b_r * 180 / 3.14159)
        angle_c = round(angle_c_r * 180 / 3.14159)
        angles = [angle_a, angle_b, angle_c]
        angles.sort()
        return angles



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

