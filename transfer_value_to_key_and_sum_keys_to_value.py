def add_value_to_key(y, k, v):  # add_val
    if k in y.keys():
        y[k] = y[k] + v
    else:
        y[k] = v


def sum_values_over_keys(x):  # sum_kv
    y = {}
    for k, v in x:
        add_value_to_key(y, k, v)
    return y


if __name__ == '__main__':
    x = [(1, 2), (4, 3), (4, 5)]
    ans = sum_values_over_keys(x)
    print(ans[4])
