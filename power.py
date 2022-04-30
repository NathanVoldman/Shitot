def B(x, z):
    w = 0
    for _ in range(z):
        w = w + x
    return w


def A(x, y):
    z = 1
    for _ in range(y):
        z = B(x, z)
    return z


if __name__ == "__main__":
    x, y = 2, 5
    z = A(x, y)
    print(z)

    
# multiply - B
# power - A
# Answers:
# 1.32
# 2.25
# 3.10
# 4.7
