user_input = input("Enter some text: ")

counter = {}

for a in user_input:
    if a in counter:
        counter[a] += 1
    else:
        counter[a] = 1

for a, count in counter.items():
    print(f"{a} = {count}")


