from read import read_furniture_data
from submain import for_choice_2,for_choice_3

def main():
    '''
    Description: Provides a menu-driven interface for the BRJ Furniture Store Management System. 
    The function continuously displays a menu with options to display available furniture, 
    purchase furniture from the manufacturer, sell furniture to customers, or exit the program.
    Based on user input, it calls corresponding functions to handle each operation.
    
    Arguments: none
    
    Return: none

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
            print("\n---------------Exiting-----------------\n")
            print("\n-----------------------------------------")
            print("Thank you for choosing BRJ Furniture.")
            print("-----------------------------------------\n")
            break
        
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == '__main__':
    main()