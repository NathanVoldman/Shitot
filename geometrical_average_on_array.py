import math


def array_of_tuples_from_each_consecutive_items(x):  # tup_adj
    y = []
    for i in range(len(x) - 1):
        y.append((x[i], x[i + 1]))
    return y


def euclidian_distance(x1,x2):  # dist  #A
    '''
    Rewrite This!!!!
    :param x1:
    :param x2:
    :return:
    '''
    y = array_of_tuples_from_each_consecutive_items(x1,x2)
    w = 0
    for z in y:
        w += sum(z)
    ans = math.sqrt(w)
    return ans


if __name__ == '__main__':
    x1 = [1, 3, 5, 3]
    x2 = [1, 3, 5, 3]
    ans = norm_2(x1,x2)
    print(ans)
