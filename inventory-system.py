import json

class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def add_stock(self, amount):
         if amount > 0:
            self.quantity += amount
            return True

         return False

    def stock_value(self):
        return self.price * self.quantity
    
    def remove_stock(self, amount):
        if (amount <= self.quantity) and (amount > 0):
           self.quantity -= amount
           return True
        else:
            return False
    
    def __str__(self):
        return f"{self.name} | {self.price} | {self.quantity} | {self.category}"

    def to_dict(self):
        return{
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["price"],
            data["quantity"],
            data["category"]
        )
    
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            print(product)

    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.stock_value()

        return total

    def find_product(self, name):
        for product in self.products:
            if product.name.lower().strip() == name.lower().strip():
                return product
            
        return None    

    def remove_product(self, name):
        product = self.find_product(name)
        if product is not None:
            self.products.remove(product)
            print("Product removed successfully!")
            return True
        print("Product not found!")
        return False 

    def product_exists(self, name):
        return self.find_product(name) is not None

    def to_dict(self):
        return{
            "products": [product.to_dict() for product in self.products] 
        }

    def save_inventory(self):
        try:
            with open("inventory.json", "w") as file:
                json.dump(self.to_dict(), file, indent=4)

            return True
        
        except OSError:
            return False
        
    def load_inventory(self, filename="inventory.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("No saved inventory found. Start with an empty inventory.")
            return
        except json.JSONDecodeError:
            print("Inventory file is invalid or corrupted.")
            return


        self.products = []

        for product_data in data["products"]:
            product = Product.from_dict(product_data)
            self.products.append(product)
            
def menu():
    print("\n========================\n" 
        "  INVENTORY MANAGEMENT\n"
        "========================\n"
        "\n 1. Add Product" 
        "\n 2. View products" 
        "\n 3. Search product" 
        "\n 4. Remove product" 
        "\n 5. Add stock" 
        "\n 6. Remove stock"
        "\n 7. Total inventory value" 
        "\n 8. Save inventory" 
        "\n 9. Exit")

inventory = Inventory()
inventory.load_inventory()

def get_product_name():
    while True:
        name = input("Enter product's name: ").strip()
        if not name:
            print("Product name cannot be empty.")
            continue
        break

while True:
    menu()
    try:
        choice = int(input("Select and option: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice < 1 or choice > 9:
        print("Please select an option between 1 and 9.")
        continue

    if choice == 1:
        name = get_product_name()
        if inventory.product_exists(name):
            print("A product with that name already exists.")
            continue

        while True:
            try:
                price = int(input("Enter product's price: "))
                if price < 0:
                    print("Price cannot be negative.")
                    continue

                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                quantity = int(input("Enter product's quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        while True:
            category = input("Enter product's category: ").strip()

            if not category:
                print("Category cannot be empty.")
                continue
            break

        product = Product(name, price, quantity, category)
        inventory.add_product(product)

        print("Product added successfully!")
        print(product)
        continue

    elif choice == 2:
        print("Available products:")
        inventory.display_products()   

    elif choice == 3:
        name = get_product_name()   

        product = inventory.find_product(name)

        if product is not None:
            print(product)
        else:    
            print("Product not found.")
            continue

    elif choice == 4:
        name = get_product_name()      
        inventory.remove_product(name)
        continue

    elif choice == 5:
        name = get_product_name()     

        find_product = inventory.find_product(name)

        if find_product is not None:
            while True:
                try:
                    amount = int(input("Enter quantity/stock amount: "))
                    if amount <= 0:
                        print("Stock must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")

            find_product.add_stock(amount)

            print("Stock updated successfully!")
            print(find_product)
        else:
            print("Product not found.")
        continue

    elif choice == 6:
        name = get_product_name()    

        product = inventory.find_product(name)

        if product is not None:
            while True:
                try:
                    amount = int(input("Enter quantity/stock amount: "))
                    if amount <= 0:
                        print("Stock amount must be greater that 0.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")

            result = product.remove_stock(amount)

            if result:
                print("Stock removed successfully")
                print(product)
            else:
                print("Stock removal failed.")
        else:
            print("Product not found.")
        continue

    elif choice == 7:
        total = inventory.total_inventory_value()
        print(f"Total inventory value: {total}")
        continue

    elif choice == 8:
        result = inventory.save_inventory()

        if result:
            print("Inventory saved successfully!")
        else:
            print("Could not save inventory.")

        continue    

    elif choice == 9:
        ask = input("Are you sure you want to exit? (y/n): ")

        if ask.lower().strip() == "y":
            print("Goodbye!")
            break
        elif ask.lower().strip() == "n":
            continue
        else:
            print("Enter either y / n.")
        continue