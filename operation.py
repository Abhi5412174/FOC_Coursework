import datetime
from write import write_inventory, add_new_product
from read import read_inventory
from write import order_Invoice,sell_invoice
import random

def update_inventory(furniture_id, quantity_change):
    inventory = read_inventory()
    for item in inventory:
        if item[0] == furniture_id:
            current_quantity = int(item[3])
            new_quantity = current_quantity + quantity_change
            item[3] = str(new_quantity)
            break
    write_inventory(inventory)

def order_furniture(furniture_id, quantity, employee_name, transactions):
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
    filename = f'order_invoice_of_{transactions[0]["employee_name"]}_{datetime.datetime.now().strftime("%Y%m%d%H%M")}.txt'
    furniture_ids = []
    manufacturers = []
    product_names = []
    quantities = []
    price_per_units = []
    item_totals = []
    subtotal = 0
    shipping_cost = random.choice([10,20,30,40,50,60])

    for transaction in transactions:
        furniture_ids.append(transaction["furniture_id"])
        manufacturers.append(transaction["manufacturer"])
        product_names.append(transaction["product_name"])
        quantities.append(str(transaction["quantity"]))
        price_per_units.append(f"${transaction['price_per_unit']:.2f}")
        item_totals.append(f"${transaction['total_cost']:.2f}")
        subtotal += transaction["total_cost"]
    
    grand_total = subtotal + shipping_cost
    order_Invoice(furniture_ids, manufacturers, product_names, quantities, transactions, price_per_units, item_totals, subtotal, shipping_cost, grand_total, filename)

def sell_furniture(customer_name, transactions):
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
                else:
                    print("\nSome transactions could not be processed.")
                    print("You may have entered more Quantities of products than inventory.")
                    print("Please enter the valid furniture ID to proceed further.")
                    print("Thank You!")
                break
        
        if not product_found:
            invalid_transactions.append({"furniture_id": transaction["furniture_id"], "error": "Not available in inventory."})

    if valid_transactions:
        print("\nIf you are outside the valley, you may incur extra shipping costs.")
        location = input("\nYour Location (1 for inside valley / 2 for outside valley): ")
        print("------------------------------------------------------------------")
        
        if location == "2":
            shipping_cost = 50

        grand_total = subtotal + vat_amount + shipping_cost

        filename = f'sale_invoice_of_{customer_name}_{datetime.datetime.now().strftime("%Y%m%d%H%M")}.txt'
        
        sell_invoice(filename, customer_name, valid_transactions, subtotal, vat_amount, shipping_cost, grand_total)

        