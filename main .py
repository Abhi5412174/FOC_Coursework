from read import read_furniture_data
from submain import for_choice_2,for_choice_3

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
            for_choice_2()
            
        elif choice == "3":
            for_choice_3()
            
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