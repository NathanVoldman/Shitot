def word_has_letter(x, y):
    for a in x:
        if a.lower() == y.lower():
            return True
    return False


def find_words_with_letter(x_list, y):
    z = []
    for x in x_list:
        if word_has_letter(x, y):
            z.append(x)
    return z


if __name__ == "__main__":
    x_list = ['hello', 'are', 'grow', 'spam', 'ham', 'hi', 'go', 'to', 'this']
    y = 'h'
    print(find_words_with_letter(x_list, y))


#     def has_let(x, y):
#         for a in x:
#             if a.lower() == y.lower():
#                 return True
#         return False


#     def wrd_w_let(x_list, y):
#         z = []
#         for x in x_list:
#             if has_let(x, y):
#                 z.append(x)
#         return z


#     if __name__ == "__main__":
#         x_list = ['hello', 'are', 'grow', 'spam', 'ham', 'hi', 'go', 'to', 'this']
#         y = 'h'
#         print(wrd_w_let(x_list, y))

    
# def B(x, y):
#     for a in x:
#         if a.lower() == y.lower():
#             return True
#     return False


# def A(x_list, y):
#     z = []
#     for x in x_list:
#         if B(x, y):
#             z.append(x)
#     return z


# if __name__ == "__main__":
#     x_list = ['hello', 'are', 'grow', 'spam', 'ham', 'hi', 'go', 'to', 'this']
#     y = 'h'
#     print(A(x_list, y))

# answers:

# [are,grow,spam,go,to]
# [hello,ham,hi]
# [hello,ham,hi,this]
# [hello,are,grow,spam,ham,hi,go,to,this]
# []
