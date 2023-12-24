# program using dictionary to simulate concession stand

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("-------------- MENU ----------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is None:
        print(f"Sorry, {food} is not on the menu. Pick items from the menu")
    else:
        cart.append(food)
        # I can calculate total outside while loop
        # total += menu[food]

print("------------------------------------")
print(f"This is your order: ")
counter = 1
for food in cart:
    print(f"{counter}. {food}")
    counter += 1

for food in cart:
    total += menu.get(food)

print(f"\nTotal price is: ${total:.2f}")
