def sure_not(line):
    line_list = line.split()
    line_list_new = ["not"]
    if line_list[0] == "not":
        line_list_new = line_list
    else:
        for item in line_list:
            line_list_new.append(item)
    line_new = " ".join(line_list_new)
    return line_new

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sure_not("sure") == "not sure", "1st example";
    assert sure_not("not sure") == "not sure", "2st example";
    assert sure_not("noter") == "not noter", "3st example";

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

