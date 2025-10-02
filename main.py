import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def list_all_products():
    """ prints a list of all products in store along with price and quantity"""
    print("\n\tList of Products\n\t________________")
    if best_buy.get_all_products():
        for index, product in enumerate(best_buy.get_all_products()):
            print(f"{index + 1}.\t{product.show()}, Price: {product.get_price()}, Quantity: {product.get_quantity()}")
    else:
        print("No products available")


def show_total_amount_in_store():
    """ Shows total amount of items in store"""
    print(f"\nTotal of {best_buy.get_total_quantity()} items in Store")


def make_an_order():
    """
    Prints a list of products along with price and quantity
    Prompts user to select product(s) and quantity
    Creates list with tuples: [(product, quantity)]
    makes an order
    Prints total price
    """
    shopping_list = []
    product_table = {}

    print("\n\tYour Order\n\t___________")
    if not best_buy.get_all_products():
        print("No products available.")
        return

    # creat dict to store dispatch table for all products available
    for index, product in enumerate(best_buy.get_all_products()):
        product_table[index + 1] = product


    # print menu
    for key, product in product_table.items():
        print(f"{key}.\t{product.show()},Price: {product.get_price()},Quantity: {product.get_quantity()}")
    print("_" * 30)
    print("When you want to finish order, enter empty text.")

    # prompt user to order (product and quantity)
    while True:
        users_order = input("Which product do you want? ")
        product_quantity = input("What amount do you want? ")
        if not users_order or not product_quantity:
            break
        try:
            users_order = int(users_order)
            product_quantity = int(product_quantity)
            if users_order not in product_table:
                print(f"Number {users_order} not in list.")
                continue
            if product_quantity <= 0:
                print(f"Quantity must be greater than zero.")
                continue
            shopping_list.append((product_table[users_order], product_quantity))
            total_price = best_buy.order(shopping_list)
            print(f"Order made! Total payment: {total_price}")
        except ValueError:
            print("Please enter numbers only")
        except Exception as e:
            print(f"Unfortunately somthing went wrong. Error: {e}")
    return

def quit_program():
    """ quits program"""
    print("Good by!")
    exit()


def start():
    """ prints menu and prompts user to choose"""
    while True:
        # menu dispatch table
        menu_table = {
            1: ["List all products in store", list_all_products],
            2: ["Show total amount in store", show_total_amount_in_store],
            3: ["Make an order", make_an_order],
            4: ["Quit", quit_program]
        }

        # Print menu
        print("\n\tStore Menu\n\t__________")
        for key, item in menu_table.items():
            print(f"{key}.\t{item[0]}")
        try:
            user_choice = int(input("Please choose a number: "))
            if user_choice not in menu_table:
                print(f"Number {user_choice} not in list.")
                continue
            menu_table[user_choice][1]()
        except ValueError:
            print("please enter a number")


def main():
    start()


if __name__ == "__main__":
    main()
