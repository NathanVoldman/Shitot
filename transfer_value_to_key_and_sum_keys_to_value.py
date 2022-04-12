def append_value_to_key(my_dict, key, value): # append_val
    my_dict[key] = my_dict.get(key, 0) + value


def switch_key_and_value_and_sum_over_new_keys(src_dict): # switch_sum
    target_dict = dict()
    for key, value in src_dict.items():
        append_value_to_key(target_dict, value, key)
    return target_dict


def main():
    my_dict = {1:2, 3:4, 5:4}
    new_dict = switch_key_and_value_and_sum_over_new_keys(my_dict)
    print(new_dict)


if __name__ == '__main__':
    main()
