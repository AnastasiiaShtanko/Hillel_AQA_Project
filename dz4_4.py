user_input = input("Enter some text: ")

character_count = {}

for char in user_input:
    if char in character_count:
        character_count[char] += 1
    else:
        character_count[char] = 1

for char, count in character_count.items():
    print(f"{char} = {count}")
