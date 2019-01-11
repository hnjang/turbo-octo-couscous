def count_words(text: str, words: set) -> int:
    t_text = text.lower()
    cnt = 0
    for w in words:
        idx = t_text.find(w)
        if idx == -1: continue
        cnt += 1
        t_text.replace(w, '')
    return cnt


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("LOLOLOLOLOL?", {"lol", "olo"}) == 2, "Example"
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
