import datetime
from write import write_inventory, add_new_product
from read import read_inventory

def update_inventory(furniture_id, quantity_change):
    inventory = read_inventory()
    for item in inventory:
        if item[0] == furniture_id:
            current_quantity = int(item[3])
            new_quantity = current_quantity + quantity_change
            item[3] = str(new_quantity)
            break
    write_inventory(inventory)

def order_furniture(furniture_id, quantity, employee_name):
    product_list = read_inventory()
    product_found = False
    
    for item in product_list:
        if item[0] == furniture_id:
            product_found = True
            update_inventory(furniture_id, quantity)
            price_per_unit = float(item[4].replace('$', ''))
            total_cost = quantity * price_per_unit
            
            with open(f'order_invoice_of_{employee_name}_{datetime.datetime.now().strftime("%Y%m%d%H%M")}.txt', 'w') as file:
                file.write(f"Order Invoice\n")
                file.write("----------------------------\n")
                file.write(f"Furniture ID: {furniture_id}\n")
                file.write(f"Manufacturer: {item[1]}\n")
                file.write(f"Product Name: {item[2]}\n")
                file.write(f"Quantity Ordered: {quantity}\n")
                file.write(f"Employee Name: {employee_name}\n")
                file.write(f"Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                file.write("----------------------------\n")
                file.write(f"Total Cost: ${total_cost:.2f}\n")
            break
    
    if not product_found:
        print("\nThis product is not in inventoory so adding the item in inventory......\n")
        manufacturer = input("Enter manufacturer name: ")
        product_name = input("Enter product name: ")
        price = input("Enter price per unit (e.g. $50): ")
        add_new_product(furniture_id, manufacturer, product_name, quantity, price)
        # After adding the new product, place the order again
        order_furniture(furniture_id, quantity, employee_name)


def sell_furniture(customer_name, furniture_id, quantity):
    inventory = read_inventory()
    for item in inventory:
        if item[0] == furniture_id:
            price_per_unit = float(item[4].replace('$', ''))
            total_cost = quantity * price_per_unit
            vat_amount = total_cost * 0.13
            print("If you are outside the vally than you may got extra charge of shipping cost.\n")
            location = input("\nYour Location (1 for inside vally / 2 for outside vally. ): ")
            print("------------------------------------------------------------------")
            
            if location == "2":
                shipping_cost = 50
                total_amount = total_cost + vat_amount + shipping_cost
                    
            else:
                shipping_cost = 0
                total_amount = total_cost + vat_amount + shipping_cost
                
            if int(item[3]) >= quantity:
                update_inventory(furniture_id, -quantity)
                
                with open(f'sale_invoice_of_{customer_name}_{datetime.datetime.now().strftime("%Y%m%d%H%M")}.txt', 'w') as file:
                    file.write(f"Sale Invoice\n")
                    file.write("----------------------------\n")
                    file.write(f"Customer Name: {customer_name}\n")
                    file.write(f"Furniture ID: {furniture_id}\n")
                    file.write(f"Brand: {item[1]}\n")
                    file.write(f"Product Name: {item[2]}\n")
                    file.write(f"Quantity Sold: {quantity}\n")
                    file.write(f"Price per Unit: {item[4]}\n")
                    file.write(f"Date and Time: {datetime.datetime.now().strftime("%Y-%m-%d- %H:%M")}\n")
                    file.write(f"Total Cost without Shipping: ${total_cost:.2f}\n")
                    file.write(f"Shipping Cost: ${shipping_cost:.2f}\n")
                    file.write(f"VAT (13%): ${vat_amount:.2f}\n")
                    file.write("----------------------------\n")
                    file.write(f"Total Amount to be Paid: ${total_amount:.2f}\n")
                break
            else:
                print("Insufficient stock available.")
                break
