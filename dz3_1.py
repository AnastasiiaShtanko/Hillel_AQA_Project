def shopping():
    print('*** Your shopping list ***')
    products = input("Please add products to the list using a space: ")
    products_list = products.split()

    if not any(products_list):
        print("List is empty!")
        return
    else:
        print(f"Your products list: {products_list}")

    while len(products_list) != 0:
        operation = input('\nDo you want to edit your products list?\nEnter + to add\nEnter - to remove\n')

        if operation == "+":
            new_product = input('Enter the product: ')
            products_list.append(new_product)

        elif operation == "-":
            if not any(products_list):
                print("List is already empty!")
            else:
                removed_product = input("Enter product to remove: ")
                if removed_product in products_list:
                    products_list.remove(removed_product)
                else:
                    print(f"There is no {removed_product} in the list.")
        else:
            print("Incorrect operation!")
        print("Your updated products list:", products_list)

    print("List is empty! End of the program")


shopping()
