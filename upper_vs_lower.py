def count_upper(x): # cntu
    y = 0
    for c in x:
        if c.isupper():
            y += 1
    return y

def count_lower(x): # cntl
    y = 0
    for c in x:
        if c.islower():
            y += 1
    return y

def is_more_lower_letters(x):
    z = count_lower(x) > count_upper(x)
    return z

if __name__=='__main__':
    x = 'ExPlAiNeD'
    is_more_lower_letters(x)

# Answers:
# True
# False
