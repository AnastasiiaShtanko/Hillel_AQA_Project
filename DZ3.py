def shopping():
    products_list = input("Please add products using a space: ")
    products = products_list.split()
    print("Your products list: ", products)

    if not any(products_list):
        print("Product list is empty!")
    action = input("Do you want to edit your products list? (+product to add, -product to remove)")


shopping()