VOWELS = "aeiouy"

def translate(phrase):
    phrase_list = phrase.split()
    new_phrase_list = []
    for word in phrase_list:
        new_word = ""
        count = 0
        c_pre = ""
        for c in word:
            if c not in VOWELS:
                new_word += c
                count = 0
                c_pre = ""
            else:
                if c == c_pre:
                    count += 1
                    if count == 1:
                        new_word += c
                    elif count == 3:
                        count = 0
                else:
                    count = 0
                c_pre = c
        new_phrase_list.append(new_word)
    new_phrase = " ".join(new_phrase_list)
    return new_phrase


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
