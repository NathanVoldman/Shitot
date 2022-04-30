def B(z, x):
    ''' This function does ??? '''
    ans = 0
    for _ in range(z):
        ans += x
    return ans


def A(x, y):
    ''' This function does ??? '''
    ans = 1
    for _ in range(y):
        ans = B(ans, x)
    return ans


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
