# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    sorted_list = sorted(products_list, key=lambda x: x[1], reverse=sort_order == 'desc')
    return sorted_list

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")

def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")

# def add_to_cart(cart, product, quantity):
#     cart.append((product, quantity))
def add_to_cart(cart, product, quantity):
    cart.append((product + (quantity,)) if isinstance(product, tuple) else (product, quantity))


# def display_cart(cart):
#     if not cart:
#         print("Your cart is empty.")
#     else:
#         total_cost = 0
#         for product_info in cart:
#             product_name, product_price, quantity = product_info  # 正确解包三元组
#             total_cost += product_price * quantity
#         print("Items in your cart:")
#         for product_info in cart:
#             product_name, product_price, quantity = product_info  # 正确解包三元组
#             print(f"{product_name} - Quantity: {quantity} - Total: ${product_price * quantity}")
#         print(f"Total cost: ${total_cost}")
def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        total_cost = 0
        print("Items in your cart:")
        for product_info in cart:
            product_name, product_price, quantity = product_info
            total_cost += product_price * quantity
            print(f"{product_name} - ${product_price} x {quantity} = ${product_price * quantity}")
        print(f"Total cost: ${total_cost}")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Receipt for {name}, {email}")
    print(f"Items ordered:")
    for product, quantity in cart:
        product_name, product_price = product
        print(f"{product_name} - ${product_price} x {quantity}")
    print(f"Total cost: ${total_cost}")
    print(f"Delivery address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

def main():
    cart = []  # 初始化购物车
    name = input("Please enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter your first and last name using only letters.")
        name = input("Please enter your name: ")

    email = input("Please enter your email address: ")
    while not validate_email(email):
        print("Invalid email address. Please include an @ sign.")
        email = input("Please enter your email address: ")

    while True:
        display_categories()
        category_choice = input("Please enter the number of the category you would like to explore or 4 to exit shopping: ")
        if category_choice.isdigit():
            if int(category_choice) == 4:
                address = input("Please enter your delivery address: ")
                if cart:
                    total_cost = 0
                    for product_info in cart:
                        product_name, product_price, quantity = product_info
                        total_cost += product_price * quantity
                    generate_receipt(name, email, cart, total_cost, address)
                print("Thank you for using our portal. Have a nice day.")
                break
            elif 1 <= int(category_choice) <= len(products):
                selected_category = list(products.keys())[int(category_choice) - 1]
                products_list = products[selected_category]
                display_products(products_list)

                while True:
                    product_choice = input("Select an option: \n1. Select a product to buy\n2. Sort the products according to the price.\n3. Go back to the category selection.\n4. Finish shopping\n: ")
                    if product_choice == "1":
                        while True:
                            try:
                                product_number = int(input("Enter the number of the product you want to buy: "))
                                product, price = products_list[product_number - 1]
                                quantity = int(input("Enter the quantity: "))
                                add_to_cart(cart, (product, price), quantity)
                                break
                            except (ValueError, IndexError):
                                print("Invalid product number or quantity. Please try again.")
                    elif product_choice == "2":
                        sort_order = input("Enter 1 for ascending or 2 for descending order: ")
                        sort_order = 'asc' if sort_order == '1' else 'desc'
                        sorted_products = display_sorted_products(products_list, sort_order)
                        display_products(sorted_products)
                    elif product_choice == "3":
                        break
                    elif product_choice == "4":
                        address = input("Please enter your delivery address: ")
                        total_cost = 0
                        for product_info in cart:
                            product_name, product_price, quantity = product_info
                            total_cost += product_price * quantity
                        generate_receipt(name, email, cart, total_cost, address)
                        print("Thank you for using our portal. Have a nice day.")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Invalid category selection. Please try again.")
        else:
            print("Invalid input. Please enter a number.")

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
