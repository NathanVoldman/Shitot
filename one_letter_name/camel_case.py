def A(y):
    z = y[0].upper()
    z+= y[1:]
    return z

def B(x):
    ans = []
    x = x.split(' ')
    for y in x:
        z = A(y)
        ans.append(z)
    return ''.join(ans)


if __name__=="__main__":
    x = 'this is a test string'
    print(B(x))
