import math


def difference_vector(x1, x2):
    assert len(x1) == len(x2)
    y = []
    for i in range(len(x1)):
        y.append(x1[i] - x2[i])
    return y


def euclidian_distance(x1, x2):
    y = difference_vector(x1, x2)
    z = 0
    for i in range(len(y)):
        z += y[i] ** 2
    ans = math.sqrt(z)
    return ans


if __name__ == '__main__':
    x1 = [1, 2, 3]
    x2 = [1, 6, 6]
    ans = euclidian_distance(x1, x2)
    print(ans)

    
    
    
# import math


# def B(x1, x2):
#     assert len(x1) == len(x2)
#     y = []
#     for i in range(len(x1)):
#         y.append(x1[i] - x2[i])
#     return y


# def A(x1, x2):
#     y = B(x1, x2)
#     z = 0
#     for i in range(len(y)):
#         z += y[i] ** 2
#     ans = math.sqrt(z)
#     return ans


# if __name__ == '__main__':
#     x1 = [1, 2, 3]
#     x2 = [1, 6, 6]
#     ans = A(x1, x2)
#     print(ans)

    
    
    
# import math


# def diff(x1, x2):
#     assert len(x1) == len(x2)
#     y = []
#     for i in range(len(x1)):
#         y.append(x1[i] - x2[i])
#     return y


# def dist(x1, x2):
#     y = diff(x1, x2)
#     z = 0
#     for i in range(len(y)):
#         z += y[i] ** 2
#     ans = math.sqrt(z)
#     return ans


# if __name__ == '__main__':
#     x1 = [1, 2, 3]
#     x2 = [1, 6, 6]
#     ans = dist(x1, x2)
#     print(ans)
