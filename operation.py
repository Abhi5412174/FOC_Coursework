import datetime
from write import write_inventory, add_new_product
from read import read_inventory
from write import order_Invoice,sell_invoice

def update_inventory(furniture_id, quantity_change):
    '''
    Description: Updates the quantity of a specific furniture item in the inventory.
    The function reads the current inventory from "inventory.txt", adjusts the quantity of the item
    with the given furniture ID by the specified quantity change, and writes the updated inventory back
    to the file.

    Arguments: 
    furniture_id : The ID of the furniture item whose quantity needs to be updated.
    quantity_change : The amount by which to change the item's quantity. This can be positive (to add) or negative (to remove).

    Return: 
    None

    '''
    inventory = read_inventory()
    for item in inventory:
        if item[0] == furniture_id:
            current_quantity = int(item[3])
            new_quantity = current_quantity + quantity_change
            item[3] = str(new_quantity)
            break
    write_inventory(inventory)

def order_furniture(furniture_id, quantity, employee_name, transactions):
    '''
    Description: Processes an order for a specific furniture item. The function checks if the item is present
    in the inventory, updates its quantity if available, and adds the order details to the transaction list.
    If the item is not found in the inventory, it prompts the user to enter the item's details, adds the item
    to the inventory, and then processes the order.

    Arguments: 
    furniture_id : The ID of the furniture item being ordered.
    quantity : The quantity of the furniture item being ordered.
    employee_name : The name of the employee handling the order.
    transactions : A list where each dictionary represents a transaction and includes details
    such as furniture ID, manufacturer, product name, quantity, price per unit, and total cost.

    Return: 
    None

    '''
    product_list = read_inventory()
    product_found = False
    
    for item in product_list:
        if item[0] == furniture_id:
            product_found = True
            update_inventory(furniture_id, quantity)
            price_per_unit = float(item[4].replace('$', ''))
            total_cost = quantity * price_per_unit
            
            transactions.append({
                "furniture_id": furniture_id,
                "manufacturer": item[1],
                "product_name": item[2],
                "quantity": quantity,
                "employee_name": employee_name,
                "price_per_unit": price_per_unit,
                "total_cost": total_cost
            })
            break
    
    if not product_found:
        print("\nThis product is not in inventory. Adding the item to inventory...\n")
        manufacturer = input("\nEnter manufacturer name: ")
        product_name = input("Enter product name: ")
        price = input("Enter price per unit (e.g., $50): ")
        add_new_product(furniture_id, manufacturer, product_name, quantity, price)
        order_furniture(furniture_id, quantity, employee_name, transactions)

def generate_invoice(transactions):
    '''
    Description: Generates an order invoice based on the provided transactions and saves it to a file. 
    The invoice includes details such as furniture IDs, manufacturers, product names, quantities, 
    price per unit, item totals, subtotal, shipping cost (gives the choice to input the location in the form of really far, far and near), and grand total.
    The filename is created using the employee's name and the current date and time.

    Arguments: 
    transactions : A list of dictionaries where each dictionary represents a transaction
    with details such as furniture ID, manufacturer, product name, quantity, price per unit, and total cost.

    Return: 
    None
    
    '''
    filename = f'order_invoice_of_{transactions[0]["employee_name"]}_{datetime.datetime.now().strftime("%Y%m%d%H%M")}.txt'
    furniture_ids = []
    manufacturers = []
    product_names = []
    quantities = []
    price_per_units = []
    item_totals = []
    subtotal = 0
    vat_amount = 0
    print("\nHow far is the manufacture's Factrory from your location?")
    distanceChecker = input("1. for more than 5 Km far\n2. for 2 Km far or more\n3. for less than 2 Km far: ")
    if distanceChecker == "1":
        shipping_cost = 100
    elif distanceChecker == "2":
        shipping_cost = 60
    else:
        shipping_cost = 40

    for transaction in transactions:
        furniture_ids.append(transaction["furniture_id"])
        manufacturers.append(transaction["manufacturer"])
        product_names.append(transaction["product_name"])
        quantities.append(str(transaction["quantity"]))
        price_per_units.append(f"${transaction['price_per_unit']:.2f}")
        item_totals.append(f"${transaction['total_cost']:.2f}")
        subtotal += transaction["total_cost"]
        vat_amount = subtotal * 0.13
    
    grand_total = vat_amount + shipping_cost + subtotal
    order_Invoice(furniture_ids, manufacturers, product_names, quantities, transactions, price_per_units, item_totals, subtotal, shipping_cost, grand_total, filename,vat_amount)

def sell_furniture(customer_name, transactions):
    '''
    Description: Processes sales transactions for furniture items, updating inventory and generating a sale invoice. 
    The function checks if each item in the transaction list is available in the inventory and processes valid transactions. 
    It calculates the subtotal, VAT, and shipping cost based on the location of the customer. Invalid transactions are logged.

    Arguments: 
    customer_name : The name of the customer making the purchase.
    transactions : A list of dictionaries where each dictionary contains transaction details including furniture ID, quantity, and other transaction-related information.

    Return: 
    None
    
    '''
    inventory = read_inventory()
    subtotal = 0
    vat_amount = 0
    shipping_cost = 0
    valid_transactions = []
    invalid_transactions = []

    for transaction in transactions:
        product_found = False
        for item in inventory:
            if item[0] == transaction["furniture_id"]:
                product_found = True
                price_per_unit = float(item[4].replace('$', ''))
                total_cost = transaction["quantity"] * price_per_unit
                transaction["total_cost"] = total_cost
                transaction["price_per_unit"] = price_per_unit
                transaction["brand"] = item[1]
                transaction["product_name"] = item[2]
                
                if int(item[3]) >= transaction["quantity"]:
                    valid_transactions.append(transaction)
                    subtotal += total_cost
                    vat_amount += total_cost * 0.13
                    update_inventory(transaction["furniture_id"], -transaction["quantity"])

                break
        
        if not product_found:
            invalid_transactions.append({"furniture_id": transaction["furniture_id"], "error": "Not available in inventory."})

    if valid_transactions:
        print("\nIf you are outside the valley, you may incur extra shipping costs.")
        location = input("\nYour Location (1 for inside Sundarharaincha / 2 for outside Sundarharaincha): ")
        print("------------------------------------------------------------------")
        
        if location == "2":
            shipping_cost = 50

        grand_total = subtotal + vat_amount + shipping_cost

        filename = f'sale_invoice_of_{customer_name}_{datetime.datetime.now().strftime("%Y%m%d%H%M")}.txt'
        
        sell_invoice(filename, customer_name, valid_transactions, subtotal, vat_amount, shipping_cost, grand_total)

        