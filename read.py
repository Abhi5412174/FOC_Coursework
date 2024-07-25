def read_furniture_data():
    
    """Read furniture data from a text file."""
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
        
        # Split the lines into columns based on comma
        data = [line.strip().split(",") for line in lines]
       
        print(f"\n{'ID':<2} | {'Manufacturers':<30} | {'Product Name':<15} | {'Quantity':<6} | {'Price':<5}")
        print("-" * 75)
        
        for row in data:
            
            print(f"{row[0]:<2} | {row[1]:<30} | {row[2]:<15} | {row[3]:<6} | {row[4]:<8}")
            print("-" * 75)
            
    except FileNotFoundError:
        print(f"\nThe file 'inventory.txt' does not exist.")

def read_furniture_products():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
        
        data = [line.strip().split(", ") for line in lines]

        # Print the header
        print(f"{'ID':<2} | {'Product Name':<15} | {'Quantity':<6} | {'Price':<5}")
        print("-" * 35)

        for row in data:
            furniture_id = row[0]
            product_name = row[2]
            quantity = row[3]
            price = row[4]
            print(f"{furniture_id:<2} | {product_name:<15} | {quantity:<6} | {price:<5}")
            
    except FileNotFoundError:
        print(f"\nThe file 'inventory.txt' does not exist.")


def read_inventory():
    try: 
        with open('inventory.txt', 'r') as file:
            lines = file.readlines()
        return [line.strip().split(', ') for line in lines]
    
    except FileNotFoundError:
        print(f"\nThe file 'inventory.txt' does not exist.")