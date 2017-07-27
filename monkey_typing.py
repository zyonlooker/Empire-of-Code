def count_words(text, words):
    text_lower = text.lower()
    len_text = len(text_lower)
    word_list = []
    for word in words:
        len_word = len(word)
        idx = 0
        while idx <= len_text - len_word:
            if text_lower[idx: idx+len_word] == word:
                word_list.append(word)
            idx += 1
    result = len(set(word_list))
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

    print("All set? Click 'Check' to review your code and earn rewards!")

