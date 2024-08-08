from read import read_inventory
import datetime
# from operation import generate_invoice

def write_inventory(inventory):
    '''
    Description: Writes inventory data to a text file named "inventory.txt".
    The data is provided as a list of lists, where each inner list represents a line in the file
    and is joined by commas.

    Arguments: 
    inventory (List of lists): A list where each inner list contains values to be written to the file.
    
    Return: 
    None
    '''
    with open("inventory.txt", "w") as file:
        for item in inventory:
            file.write(", ".join(item) + "\n")

def add_new_product(furniture_id, manufacturer, product_name, quantity, price):
    '''
    Description: Adds a new product to the inventory by appending it to the existing data in "inventory.txt".
    The new product is added with the specified furniture ID, manufacturer, product name, quantity, and price.
    
    Arguments: 
    furniture_id (str): The ID of the new furniture product.
    manufacturer (str): The manufacturer of the new product.
    product_name (str): The name of the new product.
    quantity (int): The quantity of the new product.
    price (str): The price of the new product.
    
    Return: 
    None
    '''
    inventory = read_inventory()
    inventory.append([furniture_id, manufacturer, product_name, str(quantity), price])
    write_inventory(inventory)
    
def order_Invoice(furniture_ids,manufacturers,product_names,quantities,transactions,price_per_units,item_totals,subtotal,shipping_cost,grand_total,filename,vat_amount):
    '''
    Description: Generates an order invoice and writes it to a specified file. The invoice includes details
    about the ordered items, such as furniture IDs, manufacturers, product names, quantities, prices, and 
    total costs. It also includes the subtotal, shipping cost, and grand total.

    Arguments: 
    furniture_ids (List of str): The IDs of the ordered furniture items.
    manufacturers (List of str): The manufacturers of the ordered items.
    product_names (List of str): The names of the ordered products.
    quantities (List of str): The quantities of each ordered item.
    transactions (List of dict): A list containing transaction details, with the employee's name.
    price_per_units (List of str): The price per unit for each ordered item.
    item_totals (List of str): The total cost for each item.
    subtotal (float): The subtotal amount before shipping costs.
    shipping_cost (float): The cost of shipping.
    grand_total (float): The total amount including shipping costs.
    filename (str): The name of the file to which the invoice will be written.
    
    Return: 
    None

    '''
    with open(filename, 'w') as file:
        file.write(f"Order Invoice\n")
        file.write("----------------------------\n")
        file.write(f"Furniture ID: {', '.join(furniture_ids)}\n")
        file.write(f"Manufacturer: {', '.join(manufacturers)}\n")
        file.write(f"Product Name: {', '.join(product_names)}\n")
        file.write(f"Quantity Ordered: {', '.join(quantities)}\n")
        file.write(f"Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        file.write(f"Employee Name: {transactions[0]['employee_name']}\n")
        file.write(f"Price Per Unit: {', '.join(price_per_units)}\n")
        for i in range(len(furniture_ids)):
            file.write(f"Total Cost for Item {i+1} (ID {furniture_ids[i]}): {item_totals[i]}\n")
        file.write(f"Subtotal: ${subtotal:.2f}\n")
        file.write(f"VAT amount: ${vat_amount}\n")
        file.write(f"Shipping Cost: ${shipping_cost:.2f}\n")
        file.write("----------------------------------------------------\n")
        file.write(f"Grand Total Cost for all items: ${grand_total:.2f}\n")
    print(f"Invoice generated: {filename}")
    
def sell_invoice(filename, customer_name,transactions,subtotal,vat_amount,shipping_cost,grand_total):
    '''
    Description: Generates a sale invoice and writes it to a specified file. The invoice includes details
    about the sale such as customer name, furniture IDs, brands, product names, quantities sold, price per
    unit, total costs, subtotal, VAT amount, shipping cost, and grand total.

    Arguments: 
    filename (str): The name of the file to which the invoice will be written.
    customer_name (str): The name of the customer making the purchase.
    transactions (List of dict): A list of dictionaries containing transaction details, including furniture ID, brand, product name, quantity, price per unit, and total cost.
    subtotal (float): The subtotal amount before VAT and shipping costs.
    vat_amount (float): The VAT amount to be added.
    shipping_cost (float): The cost of shipping.
    grand_total (float): The total amount including VAT and shipping costs.
    
    Return: 
    None
    
    '''
    with open(filename, 'w') as file:
        file.write(f"Sale Invoice\n")
        file.write("----------------------------\n")
        file.write(f"Customer Name: {customer_name}\n")
        furniture_ids = [t["furniture_id"] for t in transactions]
        brands = [t["brand"] for t in transactions]
        product_names = [t["product_name"] for t in transactions]
        quantities = [str(t["quantity"]) for t in transactions]
        price_per_units = [f"${t['price_per_unit']:.2f}" for t in transactions]
        total_costs = [f"${t['total_cost']:.2f}" for t in transactions]
        file.write(f"Furniture ID: {', '.join(furniture_ids)}\n")
        file.write(f"Brand: {', '.join(brands)}\n")
        file.write(f"Product Name: {', '.join(product_names)}\n")
        file.write(f"Quantity Sold: {', '.join(quantities)}\n")
        file.write(f"Price per Unit: {', '.join(price_per_units)}\n")
        
        file.write(f"Subtotal: ${subtotal:.2f}\n")
        file.write(f"VAT (13%): ${vat_amount:.2f}\n")
        file.write(f"Shipping Cost: ${shipping_cost:.2f}\n")
        file.write("--------------------------------------------------\n")
        for i in range(len(furniture_ids)):
            file.write(f"Total Cost for Item {i+1} (ID {furniture_ids[i]}): {total_costs[i]}\n")
        file.write("--------------------------------------------------\n")
        file.write(f"Grand Total Amount to be Paid: ${grand_total:.2f}\n")

    print(f"Invoice generated: {filename}")