from read import read_furniture_data, read_furniture_products,read_inventory
from operation import sell_furniture, order_furniture,generate_invoice

def main():
    '''
    Description: Main function to drive the BRJ Furniture Store Management System. It provides a menu-driven interface
    to allow users to perform various operations such as displaying available furniture, purchasing furniture from 
    manufacturers, selling furniture to customers, and exiting the program. The function handles user input, manages
    transactions, and generates invoices as needed.

    Arguments:
    None
    
    Return: 
    None
    
    Raises:
    ValueError: If the user inputs invalid data for quantity or other required fields.
    '''
    while True:
        print("\n===================================================")
        print(" Welcome to BRJ Furniture Store Management System")
        print("====================================================")
        print("\n1. Display available furniture")
        print("2. Purchase furniture from manufacturer")
        print("3. Sell furniture to customer")
        print("4. Exit")
        choice = input("\nEnter your choice => | 1 | 2 | 3 | 4 | : ")
        
        if choice == "1":
            read_furniture_data()
            
        elif choice == "2": 
            transactions = []
            employee_name = input("Enter employee name: ")
            while True:
                try:    
                    print("\nItem already available in furniture's inventory are here: ")
                    read_furniture_products()
                    print("If you want to buy products that are not in inventory, enter the next ID.")
                    furniture_id = input("Enter furniture ID to order: ")
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
            
        elif choice == "3":
            transactions = []
            customer_name = input("\nEnter customer name: ")
            inventory = read_inventory()
            while True:
                try:
                    read_furniture_products()
                    furniture_id = input("\nEnter furniture ID to sell: ")
                    quantity = int(input("Enter quantity to sell: "))
                    if quantity > 0:
                        item_available = any(item[0] == furniture_id for item in inventory)
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
        
        elif choice == '4':
            print("\n------------------Exiting-----------------\n")
            print("\n-----------------------------------------")
            print("Thank you for choosing BRJ Furniture.")
            print("-----------------------------------------\n")
            break
        
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == '__main__':
    main()