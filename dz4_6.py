user_input = input("Please enter some text to count: ")
print({item: user_input.count(item) for item in set(user_input)})
