def add_value_to_key(y, k, v):
    if k in y.keys():
        y[k] = y[k] + v
    else:
        y[k] = v


def sum_values_over_keys(x):
    y = {}
    for k, v in x:
        add_value_to_key(y, k, v)
    return y


if __name__ == '__main__':
    x = [(1, 2), (4, 3), (4, 5)]
    ans = sum_values_over_keys(x)
    print(ans[4])
    
    
# def add_val(y, k, v):
#     if k in y.keys():
#         y[k] = y[k] + v
#     else:
#         y[k] = v


# def sum_kv(x):
#     y = {}
#     for k, v in x:
#         add_val(y, k, v)
#     return y


# if __name__ == '__main__':
#     x = [(1, 2), (4, 3), (4, 5)]
#     ans = sum_kv(x)
#     print(ans[4])

    
    
# def B(y, k, v):
#     if k in y.keys():
#         y[k] = y[k] + v
#     else:
#         y[k] = v


# def A(x):
#     y = {}
#     for k, v in x:
#         B(y, k, v)
#     return y


# if __name__ == '__main__':
#     x = [(1, 2), (4, 3), (4, 5)]
#     ans = A(x)
#     print(ans[4])
