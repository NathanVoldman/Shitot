def word_has_letter(x, y):  # has_let # B
    for a in x:
        if a.lower() == y.lower():
            return True
    return False


def find_words_with_letter(x_list, y):  # wrd_w_let # A
    z = []
    for x in x_list:
        if word_has_letter(x, y):
            z.append(x)
    return z


if __name__ == "__main__":
    x_list = ['hello', 'are', 'grow', 'spam', 'ham', 'hi', 'go', 'to', 'this']
    y = 'h'
    print(find_words_with_letter(x_list, y))

# answers:

# [are,grow,spam,go,to]
# [hello,ham,hi]
# [hello,ham,hi,this]
# [hello,are,grow,spam,ham,hi,go,to,this]
# []
