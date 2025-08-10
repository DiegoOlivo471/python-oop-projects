# We’re tasked with creating an online shopping cart system where users can 
# add items to their cart, view the total cost, and apply discounts based 
# on their membership type.

# Key OOP Concepts: -> mind map com melhor visualização da aplicaçãõ de cada um no site

#    Polymorphism: Implement different discount strategies based on user membership type.
#    Encapsulation: Hide internal details like product pricing from the user.
#    Inheritance: Create a base User class and extend it for RegularUser and PremiumUser.

# -----------------------------------------------------------------------------------------

# my ideia, step by step:

# 1 - Create a main class for users.
# 2 - Create a subclass for regular users and premium users.
# 3 - Each user can buy something, but theirs account type define their discounts on the products.

# -> Create a class for the shopping cart, where we can add items and later on calculate the
#    total value.


# CONCEPTS USED:
# - Class creation
# - staticmethods and logic
# - Enheritance
# - Polymorphism
# - Encapsulation

# -----------------------------------------------------------------------------------------

class User:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
    
    # NOTA: following a chat GPT tip, while defining our user type, we will
    #       call a new function which will decide if our user is a regular
    #       or premium one.

    # I used an @staticmethod because the ideia is to only logically regulate
    # the creation of an instance in a specific subclass, depending on the
    # user type given.
    @staticmethod
    def create_user(name: str, type: str):
        type = type.lower()
        if type == "regular":
            return UserRegular(name, type)
        elif type == "premium":
            return UserPremium(name, type)
        else:
            print("Invalid user type.")

    def discount(self, total):  # This method isn't called directly, but serves as a base
        return total            # for polymorphism.

# Depending on what the @staticmethod concluded, we have an user with similar methods
# but still different ones depending on the instance class.
class UserRegular(User):          # -> INHERITANCE
    def discount(self, total):
        return total

class UserPremium(User):
    def discount(self, total):
        return total * 0.9

class Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item: str, price: float, quantity: int):
        # Append a dictionary with item data to the cart's item list.
        self.items.append({'item': item, 'price': price, 'quantity': quantity})

    def calculate_total(self, user):
        total = 0
        # Sum all the item prices in the cart, keeping in mind the quantities of each one.
        for item in self.items:
            total += item['price'] * item['quantity']
        return user.discount(total)


# Creating the instances and calling the methods:

user1 = User.create_user("Alice", "Premium")
user2 = User.create_user("Beto", "Regular")
user3 = User.create_user("Carlos", "Premium")

cart1 = Cart()
cart2 = Cart()
cart3 = Cart()

cart1.add_item("Notebook", 3000, 1)   # (3000 + 3000) * 0.9 = 5400
cart1.add_item("Cellphone", 1500, 2)
cart2.add_item("Notebook", 2500, 1)   # (2500 + 240) * 1 = 2740
cart2.add_item("T-shirt", 60, 4)
cart3.add_item("Cellphone", 1500, 1)    # (1500 + 180) * 0.9 = 1512
cart3.add_item("T-shirt", 60, 3)

print(f"Total with discount: ${cart1.calculate_total(user1):.2f}")
print(f"Total with discount: ${cart2.calculate_total(user2):.2f}")
print(f"Total with discount: ${cart3.calculate_total(user3):.2f}")