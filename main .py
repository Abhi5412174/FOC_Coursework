from read import read_furniture_data, read_furniture_products
from operation import sell_furniture, order_furniture

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
            while True:
                print("\nItem already available in furniture's inventory")
                read_furniture_products()
                print("If you want to buy the products which are not in inventory than enter the next ID ")
                furniture_id = input("Enter furniture ID to order: ")
                quantity = int(input("Enter quantity to order: "))
                employee_name = input("Enter employee name: ")
                order_furniture(furniture_id, quantity,employee_name)
                order_more = input("Do you want to enter another transaction? (yes/no): ").strip().lower()
                if order_more != "yes":
                    break
                
        elif choice == "3":
            while True:
                customer_name = input("Enter customer name: ")
                read_furniture_products()
                furniture_id = input("Enter furniture ID to sell: ")
                quantity = int(input("Enter quantity to sell: "))
                sell_furniture(customer_name, furniture_id, quantity)
                sell_more = input("Do you want to sell another product? (yes/no): ").strip().lower()
                if sell_more != "yes":
                    break
        
        elif choice == '4':
            print("-----------------------------------------")
            print("Thank you for choosing BRJ Furniture.")
            print("-----------------------------------------")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    main()