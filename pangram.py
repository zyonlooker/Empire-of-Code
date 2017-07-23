def check_pangram(text):
    table_init = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0,\
                  "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,\
                  "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0,\
                  "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
                  
    table_check = table_init.copy()
    text_list = text.split()
    for word in text_list:
        for c in word:
            if c.isalpha() and c.lower() in table_check:
                table_check[c.lower()] += 1
    for key in table_check:
        if table_check[key] == 0:
            return False
    return True

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"

    print("All done? Earn rewards by using the 'Check' button!")

