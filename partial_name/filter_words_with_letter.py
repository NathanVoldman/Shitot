
def cont_let(x, y):
    for a in x:
        if a.lower() == y.lower():
            return True
    return False


def wrd_w_let(x_list, y):
    z = []
    for x in x_list:
        if word_has_letter(x, y):
            z.append(x)
    return z


if __name__ == "__main__":
    x_list = ['hello', 'are', 'grow', 'spam', 'ham', 'hi', 'go', 'to', 'this']
    y = 'h'
    print(wrd_w_let(x_list, y))
