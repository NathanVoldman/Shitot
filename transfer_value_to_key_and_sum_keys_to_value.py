def append_value_to_key(my_dict, key, value):
    my_dict[key] = my_dict.get(key, 0) + value


def transfer_value_to_key_and_sum_keys_to_value(src_dict):
    target_dict = dict()
    for key, value in src_dict.items():
        append_value_to_key(target_dict, value, key)
    return target_dict


def main():
    my_dict = dict([(1, 2), (3, 4), (5, 4)])
    new_dict = transfer_value_to_key_and_sum_keys_to_value(my_dict)
    print(new_dict)


if __name__ == '__main__':
    main()
