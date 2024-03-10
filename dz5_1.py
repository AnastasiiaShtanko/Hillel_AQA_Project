str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

int_list = list(map(int, str_list))

result = dict(map(lambda x: (x, pow(x, 2)), int_list))
print(result)


result_2 = dict(zip(int_list, [x**2 for x in int_list]))
print(result_2)
