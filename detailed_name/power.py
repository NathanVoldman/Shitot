def power(x,y):
    z = 1
    for _ in range(y):
        z = multiply(x,z)
    return z

def multiply(x,z):
    w = 0
    for _ in range(z):
        w = w+x
    return w

if __name__=="__main__":
    x, y = 2, 5
    z = power(x, y)
    print(z)
