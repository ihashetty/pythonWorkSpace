
"""
-> food
->Menu : add food, display food, get food by id, remove food 
-> cart : list , bill(separate)
"""

class Food:

    """Food class"""
    def __init__(self, id: int, name: str, category: str, price: float):
        self.id = int(id)
        self.name = str(name)
        self.category = str(category)
        self.price = float(price)

    def display(self) :
        """To display food item"""
        print(f"{self.id}  {self.name}  {self.category} : {self.price:.2f}")

class Menu:

    """Menu class"""
    def __init__(self, outlet_name: str, outlet_id: int):
        self.food_items= []
        self.outlet_name = outlet_name
        self.__outlet_id = int(outlet_id)

    def add_food(self, food_item):

        """To add food item to menu"""
        if not isinstance(food_item, Food):
            raise TypeError(f"Expected Food, got {type(food_item).__name__}")

        if any(item.id == food_item.id for item in self.food_items):
            raise ValueError(f"Food with id={food_item.id} already exists in the menu.")
        self.food_items.append(food_item)

    def display(self):

        """to display menu"""
        print(f"\nMenu for {self.outlet_name} (ID: {self.__outlet_id})")
        if not self.food_items:
            print("(No items yet)")
            return
        for item in self.food_items:
            item.display()

    def get_food_by_id(self, id):

        """To get food item by id"""
        for item in self.food_items:
            if item.id == id:
                return item
        return None

    def remove_food(self, id):
    
        """Remove a food item by id. Returns True if removed, False if not found."""
        for idx, item in enumerate(self.food_items):
            if item.id == id:
                del self.food_items[idx]
                return True
        return False


class Cart:

    """cart class"""
    def __init__(self):
        self.items = {}

    def add_cart(self, food, quantity):

        """add items to cart"""
        if not isinstance(food, Food):
            raise TypeError(f"Expected Food, got {type(food).__name__}")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.items[food] = self.items.get(food, 0) + quantity

    def display(self):

        """display cart items"""
        print("\nYour Cart:")
        if not self.items:
            print("Cart is empty.")
            return

        total = 0.0
        for food, qty in self.items.items():
            cost = food.price * qty
            total += cost
            print(f"{food.name} x {qty} = ₹{cost:.2f}")

        print(f"Total Bill: ₹{total:.2f}")

    def calculate_total(self):
        """to calculate total bill"""
        return sum(food.price * qty for food, qty in self.items.items())

    def clear(self):
        self.items.clear()


class FoodApp:
    def __init__(self):
        self.menu = Menu("Pizza Hut Rajajinagar", 1888)
        self.cart = Cart()
        self.load_menu()

    def load_menu(self):
        self.menu.add_food(Food(1, "Veg Pizza", "veg", 199))
        self.menu.add_food(Food(2, "Pepperoni Pizza", "non-veg", 249))
        self.menu.add_food(Food(3, "Pesto Chicken Pizza", "non-veg", 279))
        self.menu.add_food(Food(4, "Paneer Veg Pizza", "veg", 229))

    def start(self):
        while True:
            print("\n")
            print("What would you like to do?")
            print("1. View Menu")
            print("2. Add Item to Cart")
            print("3. View Cart")
            print("4. Place Order")
            print("5. Exit")
            
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.menu.display()

            elif choice == "2":
                self.menu.display()
                try:
                    food_id = int(input("Enter Food ID: ").strip())
                    qty = int(input("Enter Quantity: ").strip())
                except ValueError:
                    print("Please enter valid numeric values for ID and Quantity.")
                    continue

                food = self.menu.get_food_by_id(food_id)
                if food:
                    try:
                        self.cart.add_cart(food, qty)
                        print(f"Added to cart: {food.name} x {qty}")
                    except (TypeError, ValueError) as e:
                        print(f"Error: {e}")
                else:
                    print("Invalid Food ID.")

            elif choice == "3":
                self.cart.display()

            elif choice == "4":
                total = self.cart.calculate_total()
                if total == 0:
                    print("Cart is empty. Add items first.")
                else:
                    self.cart.display()
                    print("\nOrder Placed Successfully!")
                    print(f"Final Amount to Pay: ₹{total:.2f}")
                    self.cart.clear()
                    break

            elif choice == "5":
                print("Thank you for visiting Pizza Hut!")
                break

            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    app = FoodApp()
    app.start()
