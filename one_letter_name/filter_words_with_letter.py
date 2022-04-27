def A(x, y):
    for a in x:
        if a.lower() == y.lower():
            return True
    return False


def B(x_list, y):
    z = []
    for x in x_list:
        if A(x, y):
            z.append(x)
    return z


if __name__ == "__main__":
    x_list = ['hello', 'are', 'grow', 'spam', 'ham', 'hi', 'go', 'to', 'this']
    y = 'h'
    print(B(x_list, y))
