from read import read_furniture_data, read_furniture_products,read_inventory
from operation import sell_furniture, order_furniture,generate_invoice

def main():
    while True:
        print("\n==============================================")
        print("BRJ Furniture Store Management System")
        print("==============================================")
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
                print("\nItem already available in furniture's inventory")
                read_furniture_products()
                print("If you want to buy products that are not in inventory, enter the next ID.")
                furniture_id = input("Enter furniture ID to order: ")
                quantity = int(input("Enter quantity to order: "))

                order_furniture(furniture_id, quantity, employee_name, transactions)

                order_more = input("\nDo you want to enter another transaction? (yes/no): ").strip().lower()
                if order_more != "yes":
                    break
            generate_invoice(transactions)
                
        elif choice == "3":
            transactions = []
            customer_name = input("Enter customer name: ")
            inventory = read_inventory()  # Read inventory once at the start
            while True:
                read_furniture_products()
                furniture_id = input("Enter furniture ID to sell: ")
                quantity = int(input("Enter quantity to sell: "))

                # Check if the furniture ID is available in inventory
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

            if transactions:  # Only proceed if there are valid transactions
                sell_furniture(customer_name, transactions)
        
        elif choice == '4':
            print("\n-----------------------------------------")
            print("Thank you for choosing BRJ Furniture.")
            print("-----------------------------------------\n")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    main()