def count_upper(x):
    y = 0
    for c in x:
        if c.isupper():
            y += 1
    return y


def count_lower(x):
    y = 0
    for c in x:
        if c.islower():
            y += 1
    return y


def is_more_lower_letters(x):
    z = count_lower(x) > count_upper(x)
    return z


if __name__ == '__main__':
    x = 'ExPlAiNeD'
    print(is_more_lower_letters(x))

    
    
# def cnt_u(x):
#     y = 0
#     for c in x:
#         if c.isupper():
#             y += 1
#     return y


# def cnt_l(x):
#     y = 0
#     for c in x:
#         if c.islower():
#             y += 1
#     return y


# def more_low(x):
#     z = cnt_l(x) > cnt_u(x)
#     return z


# if __name__ == '__main__':
#     x = 'ExPlAiNeD'
#     print(more_low(x))


    
# def C(x):
#     y = 0
#     for c in x:
#         if c.isupper():
#             y += 1
#     return y


# def B(x): 
#     y = 0
#     for c in x:
#         if c.islower():
#             y += 1
#     return y


# def A(x):
#     z = B(x) > C(x)
#     return z


# if __name__ == '__main__':
#     x = 'ExPlAiNeD'
#     print(A(x))


# Answers:
# False
# True

