def capitalize(y):
    z = y[0].upper()
    z+= y[1:]
    return z

def camelcase(x):
    ans = []
    x = x.split(' ')
    for y in x:
        z = capitalize(y)
        ans.append(z)
    return ''.join(ans)


if __name__=="__main__":
    x = 'this is a test string'
    print(camelcase(x))
