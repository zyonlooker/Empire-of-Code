def clock_angle(time):
    clock_dict = {"00": 0, "01": 1, "02": 2, "03": 3, "04": 4, "05": 5,\
                  "06": 6, "07": 7, "08": 8, "09": 9, "10": 10, "11": 11,\
                  "12": 0, "13": 1, "14": 2, "15": 3, "16": 4, "17": 5,\
                  "18": 6, "19": 7, "20": 8, "21": 9, "22": 10, "23": 11}
    hour = clock_dict[time.split(":")[0]]
    minute = int(time.split(":")[1])
    ang_h = 30 * hour + minute * 0.5
    ang_m = minute * 6
    angle = ang_m - ang_h if ang_m-ang_h >= 0 else ang_h - ang_m
    if angle > 180:
        angle = 360 - angle
    return angle


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")

