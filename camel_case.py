def B(y):
    z = y[0].upper()
    z += y[1:]
    return z


def A(function_input):
    ans = []
    x = function_input.split('_')
    for y in x:
        z = B(y)
        ans.append(z)
    return ''.join(ans) # note: join is performed on the blank string here


if __name__ == "__main__":
    function_input = 'this_is_a_test_string'
    print(A(function_input))

#     def capitalize(y):
#     z = y[0].upper()
#     z += y[1:]
#     return z


# def camelcase(function_input):
#     ans = []
#     x = function_input.split('_')
#     for y in x:
#         z = capitalize(y)
#         ans.append(z)
#     return ''.join(ans) # note: join is performed on the blank string here


# if __name__ == "__main__":
#     function_input = 'this_is_a_test_string'
#     print(camelcase(function_input))

    
#  def cap(y):
#     z = y[0].upper()
#     z += y[1:]
#     return z


# def cml(function_input):
#     ans = []
#     x = function_input.split(' ')
#     for y in x:
#         z = cap(y)
#         ans.append(z)
#     return ''.join(ans)


# if __name__ == "__main__":
#     function_input = 'this is a test string'
#     print(cml(function_input))

    
# def B(y):
#     z = y[0].upper()
#     z += y[1:]
#     return z


# def A(function_input):
#     ans = []
#     x = function_input.split(' ')
#     for y in x:
#         z = B(y)
#         ans.append(z)
#     return ''.join(ans)


# if __name__ == "__main__":
#     function_input = 'this is a test string'
#     print(A(function_input))
# Answers:
# 1.ThisIsATestString
# 2.thisisateststring
# 3.This Is A Test String
# 4.this_is_a_test_string
# 5.This_Is_A_Test_String
# 6.this is a test string
