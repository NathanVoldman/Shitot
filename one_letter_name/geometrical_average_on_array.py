import math


def A(arr):
    new_arr = []
    for i in range(len(arr) - 1):
        new_arr.append((arr[i], arr[i + 1]))
    return new_arr


def B(arr):
    tup_arr = A(arr)
    product = 1
    for tup in tup_arr:
        product *= sum(tup)
    res = math.sqrt(product)
    return res


def main():
    arr = [1, 3, 5, 3]
    val = B(arr)
    print(val)


if __name__ == '__main__':
    main()
