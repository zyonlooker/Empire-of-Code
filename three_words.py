def three_words(words):
    characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    count = 0
    words_list = words.split()
    for word in words_list:
        if count == 3:
            break
        else:
            flag = 1
            for letter in word:
                if not letter in characters:
                    flag = 0
                    count = 0
                    break
            if flag == 1:
                count += 1
    if count == 3:        
        return True
    else:
        return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert three_words("Hello World hello"), "Hello"
    assert not three_words("He is 123 man"), "123 man"
    assert not three_words("1 2 3 4"), "Digits"
    assert three_words("bla bla bla bla"), "Bla Bla"
    assert not three_words("Hi"), "Hi"

    print("Earn cool rewards by using the 'Check' button!")

