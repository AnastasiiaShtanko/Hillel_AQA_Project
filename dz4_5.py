my_list = [5, 3, None, 34, 20]

for item in my_list:
    if item is None:
        print("There is None")
        break
else:
    print("There is no None")
