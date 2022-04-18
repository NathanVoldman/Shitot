def power(x,y): # pwr
    z = 1
    for _ in range(y):
        z = multiply(x,z)
    return z

def multiply(x,z): # mlt
    w = 0
    for _ in range(z):
        w = w+x
    return w

if __name__=="__main__":
    x, y = 2, 5
    z = power(x, y)
    print(z)

# Answers:
# 1.32
# 2.25
# 3.10
# 4.7