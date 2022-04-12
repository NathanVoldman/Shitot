
def main():
    x = int(input('first:'))
    y = int(input('second:'))
    print(power_plus_one(x,y))

def power_plus_one(x,y):
    ans = 1
    for _ in range(y):
        ans = multiply_plus_one(ans,x)
    return ans+1

def multiply_plus_one(x,y):
    ans = 0
    for _ in range(y):
        ans = add_plus_one(ans,x)
    return ans+1

def add_plus_one(x,y):
    return x+y+1

if __name__=="__main__":
    main()
