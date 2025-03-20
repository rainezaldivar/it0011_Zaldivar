class SmiskiFigure:
    figure_count = 0

    def __init__(self, name: str, description: str, price: float, rarity: str):
        self.id = SmiskiFigure.figure_count + 1
        self.name = self.validate_name(name)
        self.description = description
        self.price = self.validate_price(price)
        self.rarity = self.validate_rarity(rarity)
        SmiskiFigure.figure_count += 1

    @staticmethod
    def validate_name(name):
        if not name.strip():
            raise ValueError("Figure name cannot be empty.")
        return name.strip()

    @staticmethod
    def validate_price(price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        return price
    
    @staticmethod
    def validate_rarity(rarity):
        valid_rarities = ["Common", "Rare", "Limited Edition"]
        if rarity not in valid_rarities:
            raise ValueError("Invalid rarity. Choose from Common, Rare, or Limited Edition.")
        return rarity

    def update(self, name=None, description=None, price=None, rarity=None):
        if name:
            self.name = self.validate_name(name)
        if description:
            self.description = description
        if price is not None:
            self.price = self.validate_price(price)
        if rarity:
            self.rarity = self.validate_rarity(rarity)

    def __str__(self):
        return f"""ID: {self.id},
    Name: {self.name} 
    Description: {self.description}
    Price: ${self.price:.2f}
    Rarity: {self.rarity}"""


class SmiskiInventory:
    def __init__(self):
        self.figures = []

    def add_figure(self, name, description, price, rarity):
        try:
            new_figure = SmiskiFigure(name, description, price, rarity)
            self.figures.append(new_figure)
            print("Smiski figure added successfully!")
            print("")
        except ValueError as e:
            print(f"Error: {e}")
            print("")

    def update_figure(self, figure_id, name=None, description=None, price=None, rarity=None):
        figure = self.find_figure(figure_id)
        if figure:
            try:
                figure.update(name, description, price, rarity)
                print("Smiski figure updated successfully!")
                print("")
            except ValueError as e:
                print(f"Error: {e}")
                print("")

    def delete_figure(self, figure_id):
        figure = self.find_figure(figure_id)
        if figure:
            self.figures.remove(figure)
            print("Smiski figure deleted successfully!")
            print("")
        else:
            print("Figure not found.")
            print("")

    def find_figure(self, figure_id):
        for figure in self.figures:
            if figure.id == figure_id:
                return figure
        print("Figure not found.")
        print("")
        return None

    def list_figures(self):
        if not self.figures:
            print("No Smiski figures in inventory.")
            print("")
        for figure in self.figures:
            print(figure)
            print("")


if __name__ == "__main__":
    inventory = SmiskiInventory()

    while True:
        print("=============================")
        print(" Smiski Inventory Management ")
        print("=============================")
        print("1. Add Smiski Figure")
        print("2. Update Smiski Figure")
        print("3. Delete Smiski Figure")
        print("4. View Smiski Figures")
        print("5. Exit")
        choice = input("Enter your choice: ")
        print("")

        if choice == "1":
            name = input("Enter figure name: ")
            description = input("From What Series: ")
            try:
                price = float(input("Enter figure price: "))
                rarity = input("Enter rarity (Common, Secret): ")
                inventory.add_figure(name, description, price, rarity)
            except ValueError:
                print("Invalid input.")
                print("")
        elif choice == "2":
            try:
                figure_id = int(input("Enter figure ID to update: "))
                name = input("Enter new name (leave blank to keep current): ") or None
                description = input("Enter new series (leave blank to keep current): ") or None
                price_input = input("Enter new price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                rarity = input("Enter new rarity (leave blank to keep current): ") or None
                inventory.update_figure(figure_id, name, description, price, rarity)
            except ValueError:
                print("Invalid input.")
                print("")
        elif choice == "3":
            try:
                figure_id = int(input("Enter figure ID to delete: "))
                inventory.delete_figure(figure_id)
            except ValueError:
                print("Invalid input.")
                print("")
        elif choice == "4":
            inventory.list_figures()
            print("")
        elif choice == "5":
            print("Exiting program.")
            print("")
            break
        else:
            print("Invalid choice. Please try again.")
            print("")