from read import read_inventory
import datetime
# from operation import generate_invoice

def write_inventory(inventory):
    with open("inventory.txt", "w") as file:
        for item in inventory:
            file.write(", ".join(item) + "\n")

def add_new_product(furniture_id, manufacturer, product_name, quantity, price):
    inventory = read_inventory()
    inventory.append([furniture_id, manufacturer, product_name, str(quantity), price])
    write_inventory(inventory)
    
def order_Invoice(furniture_ids,manufacturers,product_names,quantities,transactions,price_per_units,item_totals,subtotal,shipping_cost,grand_total,filename):
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
        file.write(f"Shipping Cost: ${shipping_cost:.2f}\n")
        file.write("----------------------------------------------------\n")
        file.write(f"Grand Total Cost for all items: ${grand_total:.2f}\n")
    print(f"Invoice generated: {filename}")
    
def sell_invoice(filename, customer_name,transactions,subtotal,vat_amount,shipping_cost,grand_total):
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