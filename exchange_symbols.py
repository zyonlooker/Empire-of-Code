def symb_exchange(line):
    new_line = line[len(line)-1] + line[1:len(line)-1] + line[0]
    return new_line

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert symb_exchange("az") == "za", "1st example";
    assert symb_exchange("aiiiiiz") == "ziiiiia", "2st example";
    assert symb_exchange("length") == "hengtl", "3st example";

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

