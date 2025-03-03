from datetime import datetime
import json

class SuperMarket:
    def __init__(self):
        # Dictionary of available items and their prices
        self.items = {
            "rice": 20, "sugar": 30, "salt": 20, "oil": 80, "milk": 60,
            "wheatflour": 30, "gramflour": 40, "greengram": 50, "redgram": 50,
            "ginger": 40, "garlic": 40, "onions": 50, "boost": 90, "colgate": 85
        }
        self.cart = []  # List to store purchased items
        self.total_price = 0  # Total cost before GST
        self.gst = 0  # GST amount
        self.final_amount = 0  # Final payable amount

    def display_items(self):
        """Displays available items and their prices."""
        print("\nAvailable Items:")
        for item, price in self.items.items():
            print(f"{item.capitalize():<12} Rs {price}/unit")

    def add_to_cart(self):
        """Allows the user to add multiple items to the cart."""
        while True:
            item = input("Enter the item name (or type 'done' to finish): ").strip().lower()
            if item == 'done':
                break
            if item in self.items:
                try:
                    quantity = int(input(f"Enter quantity for {item}: "))
                    price = self.items[item] * quantity
                    self.cart.append({"item": item, "quantity": quantity, "price": price})
                    self.total_price += price
                    print(f"Added {quantity} {item}(s) to cart. Subtotal: Rs {self.total_price}")
                except ValueError:
                    print("Invalid quantity. Please enter a valid number.")
            else:
                print("Sorry, the item you entered is not available.")

    def generate_bill(self, name):
        """Generates the bill for the purchased items."""
        if not self.cart:
            print("Your cart is empty. No bill to generate.")
            return
        
        # Calculate GST and final amount
        self.gst = (self.total_price * 5) / 100
        self.final_amount = self.total_price + self.gst
        
        # Print the bill
        print("\n", "=" * 20, "Madhu Supermarket", "=" * 20)
        print(f"{'Name:':<10}{name:<20} {'Date:':<10}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)
        print(f"{'S.No':<5}{'Item':<15}{'Quantity':<10}{'Price':<10}")
        print("-" * 60)
        
        for idx, item in enumerate(self.cart, start=1):
            print(f"{idx:<5}{item['item'].capitalize():<15}{item['quantity']:<10}{item['price']:<10}")
        
        print("-" * 60)
        print(f"{'Total Amount:':<30} Rs {self.total_price}")
        print(f"{'GST (5%):':<30} Rs {self.gst}")
        print(f"{'Final Amount:':<30} Rs {self.final_amount}")
        print("=" * 60)
        print("Thanks for shopping with us!")
        print("=" * 60)

    def save_bill(self, name):
        """Saves the bill details to a JSON file."""
        if not self.cart:
            print("No bill to save.")
            return

        bill_data = {
            "name": name,
            "date": str(datetime.now()),
            "items": self.cart,
            "total_price": self.total_price,
            "gst": self.gst,
            "final_amount": self.final_amount
        }
        
        with open("supermarket_bill.json", "w") as file:
            json.dump(bill_data, file, indent=4)
        print("Bill saved successfully!")

# Main Program
market = SuperMarket()
name = input("Enter your name: ")

while True:
    choice = input("\nEnter 1 to view items, 2 to buy items, 3 to generate bill, 4 to exit: ")
    if choice == "1":
        market.display_items()
    elif choice == "2":
        market.add_to_cart()  # Allow multiple item purchases
    elif choice == "3":
        market.generate_bill(name)
        market.save_bill(name)
    elif choice == "4":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
