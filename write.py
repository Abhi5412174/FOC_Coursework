from read import read_inventory

def write_inventory(inventory):
    with open("inventory.txt", "w") as file:
        for item in inventory:
            file.write(", ".join(item) + "\n")

def add_new_product(furniture_id, manufacturer, product_name, quantity, price):
    inventory = read_inventory()
    inventory.append([furniture_id, manufacturer, product_name, str(quantity), price])
    write_inventory(inventory)