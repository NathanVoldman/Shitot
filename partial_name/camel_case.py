def cap(y):
    z = y[0].upper()
    z+= y[1:]
    return z

def cml_cs(x):
    ans = []
    x = x.split(' ')
    for y in x:
        z = capitalize(y)
        ans.append(z)
    return ''.join(ans)


if __name__=="__main__":
    x = 'this is a test string'
    print(cml_cs(x))
