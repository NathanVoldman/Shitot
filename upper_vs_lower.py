def count_upper(x):  # cnt_u
    y = 0
    for c in x:
        if c.isupper():
            y += 1
    return y


def count_lower(x):  # cnt_l
    y = 0
    for c in x:
        if c.islower():
            y += 1
    return y


def is_more_lower_letters(x):  # more_low
    z = count_lower(x) > count_upper(x)
    return z


if __name__ == '__main__':
    x = 'ExPlAiNeD'
    print(is_more_lower_letters(x))

# Answers:
# False
# True

