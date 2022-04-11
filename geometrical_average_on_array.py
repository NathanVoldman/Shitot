import math


def sum_dual_tuple(tup):
    tup1, tup2 = tup
    return tup1 + tup2


def geometrical_average_on_array(arr):
    product = 1
    for num in arr:
        product *= num
    res = math.sqrt(product)
    return res


def main():
    tup_arr = [(1, 1), (1, 3), (5, 3)]
    arr = [sum_dual_tuple(tup) for tup in tup_arr]
    val = geometrical_average_on_array(arr)
    print(val)


if __name__ == '__main__':
    main()
