from read import read_furniture_products,read_inventory
from operation import order_furniture, generate_invoice,sell_furniture

def for_choice_2 ():
    transactions = []
    employee_name = input("Enter employee name: ")
    if employee_name.isdigit():
       print("\nName should not contain digits. ")
    else:
        while True:
            try:    
                print("\nItem already available in furniture's inventory are here: ")
                read_furniture_products()
                print("If you want to buy products that are not in inventory, enter the next ID.")
                furniture_id = input("Enter furniture ID to order: ")
                if not furniture_id.isdigit():
                    print("\nFurniture Id should be in digit form.")
                else:
                    quantity = int(input("Enter quantity to order: "))
                    if quantity > 0:
                        order_furniture(furniture_id, quantity, employee_name, transactions)
                        order_more = input("\nDo you want to enter another transaction? (yes/no): ").strip().lower()
                        if order_more != "yes":
                            break
                    else:
                        print("\nEnter a valid Quantity (Quantity should be in positive number).")
            except ValueError:
                print("\nPlease, provide the informations carefully.")
        generate_invoice(transactions)

def for_choice_3():
    transactions = []
    customer_name = input("\nEnter customer name: ")
    if customer_name.isdigit():
        print("\nName should not contain digits. ")
    else:
        inventory = read_inventory()
        while True:
            try:
                read_furniture_products()
                furniture_id = input("\nEnter furniture ID to sell: ")
                quantity = int(input("Enter quantity to sell: "))
                if quantity > 0:
                    item_available = False
                    for item in inventory:
                        if item[0] == furniture_id:
                            item_available = True
                            if quantity >= int(item[3]):
                                print("Please enter the valid quantity.")
                                break
                    if item_available:
                        transactions.append({
                            "furniture_id": furniture_id,
                            "quantity": quantity
                        })
                    else:
                        print(f"Product ID {furniture_id} is not available in inventory.")
                    sell_more = input("\nDo you want to sell another product? (yes/no): ").strip().lower()
                    if sell_more != "yes":
                        break
                else:
                    print("\nEnter a valid Quantity (Quantity should be in positive number).\n")
            except ValueError:
                print("\nPlease, provide the informations carefully.\n")
        if transactions:
            sell_furniture(customer_name, transactions)