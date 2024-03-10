def shopping():
    print('*** Your shopping list ***')
    products = input("Please add products to the list using a space: ")

    products_list = products.split()

    if not any(products_list):
        print("List is empty!")
        return
    else:
        print("Your products list: ", products_list)

    while len(products_list) != 0:
        action = input("Do you want to edit your products list? Enter +product to add, -product to remove: ")

        if action.startswith('+'):
            new_product = action[1:]
            products_list.append(new_product)
            print(f"Product '{new_product}' has been added.")
        elif action.startswith('-'):
            removed_product = action[1:]
            if removed_product in products_list:
                products_list.remove(removed_product)
                print(f"Product '{removed_product}' has been removed.")
            else:
                print(f"There is no '{removed_product}' in the list.")
        else:
            print("Incorrect operation!")

        print("Your updated products list: ", products_list)

    print("List is empty! End of the program.")


shopping()
