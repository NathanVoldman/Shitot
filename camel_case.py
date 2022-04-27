def capitalize(y):  # cap  # B
    z = y[0].upper()
    z += y[1:]
    return z


def camelcase(function_input):  # cml  # A
    ans = []
    x = function_input.split(' ')
    for y in x:
        z = capitalize(y)
        ans.append(z)
    return ''.join(ans)


if __name__ == "__main__":
    function_input = 'this is a test string'
    print(camelcase(function_input))

# Answers:
# 1.ThisIsATestString
# 2.thisisateststring
# 3.This Is A Test String
# 4.this_is_a_test_string
# 5.This_Is_A_Test_String
# 6.this is a test string
