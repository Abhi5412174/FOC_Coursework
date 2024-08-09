from read import read_furniture_products,read_inventory
from operation import order_furniture, generate_invoice,sell_furniture

def for_choice_2 ():
    '''
    Description: Facilitates the process of placing an order for furniture by an employee. 
    The function prompts the user to enter the employee's name, select furniture items from the inventory, specify quantities,
    and then generates an invoice for the order.
    The function handles input validation for the employee's name and furniture ID, ensuring that the name does not contain digits 
    and the furniture ID is in digit form. It also ensures that the quantity is a positive number. 

    Arguments: None

    Return: None

    Exception:
    ValueError: If the user inputs an invalid value for the quantity or other required information.
    '''
    
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
    '''
    Description: Manages the process of selling furniture to a customer. The function prompts the user to enter the customer's name 
    and allows the user to select furniture items from the inventory to sell. It validates the customer's name, furniture ID, 
    and ensures that the quantity specified is available in the inventory and is a positive number. After processing the transaction(s),
    the function calls another function to complete the sale.

    Arguments: None

    Return: None

    Exception:
    ValueError: If the user inputs an invalid value for the quantity or other required information.
    '''
    
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
                            if quantity > int(item[3]):
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