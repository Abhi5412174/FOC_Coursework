def read_furniture_data():
    '''
    Description: Reads furniture data from a text file named "inventory.txt" and prints it in a tabular format.
    The text file is expected to contain lines of comma-separated values with columns for ID, Manufacturer, Product Name, Quantity, and Price.
    
    Arguments: none
    
    Return: none
    
    Exception:
    FileNotFoundError: If the file "inventory.txt" does not exist.
    '''
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
        data = []
        for line in lines:
            stripped_line = line.strip()
            split_line = stripped_line.split(",")
            data.append(split_line)
       
        print(f"\n{'ID':<2} | {'Manufacturers':<30} | {'Product Name':<15} | {'Quantity':<10} | {'Price':<5}")
        print("-" * 78)
        
        for row in data:
            print(f"{row[0]:<2} | {row[1]:<30} | {row[2]:<15} | {row[3]:<10} | {row[4]:<8}")
            print("-" * 78)
            
    except FileNotFoundError:
        print(f"\nThe file 'inventory.txt' does not exist.")

def read_furniture_products():
    '''
    Description: Reads furniture product along with ID, Manufacturer, Quantity and price data from a text file named "inventory.txt" and prints it in a tabular format.
    The text file is expected to contain lines of comma-separated values with columns.

    Arguments: 
    None
    
    Return: 
    None
    
    Exception:
    FileNotFoundError: If the file "inventory.txt" does not exist.
    '''
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
    '''
    Description: Reads inventory data from a text file named "inventory.txt" and returns it as a list of lists.
    Each list represents a line in the file, split into columns based on commas.

    Arguments: 
    None
    
    Return: 
    List of lists: Each inner list contains values from a line in the file, split by comma.
    
    Exception:
    FileNotFoundError: If the file "inventory.txt" does not exist.
    '''
    try: 
        with open('inventory.txt', 'r') as file:
            lines = file.readlines()
            result = []
            for line in lines:
                result.append(line.strip().split(', '))
            return result
    except FileNotFoundError:
        print(f"\nThe file 'inventory.txt' does not exist.")