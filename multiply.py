def multiply(x, y): # mul  # A
    ''' This function does ??? '''
    ans = 0
    for _ in range(y):
        ans += x
    return ans


if __name__ == "__main__":
    x, y = 3, 6
    ans = multiply(x, y)
    print(ans)
