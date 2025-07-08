# Question 2: Restaurant Order System (Lesson 2 - If/Elif/Else)
# Points: 10
# Create a program that takes a restaurant order and calculates the bill based on menu choices.
# Requirements:
# Display a menu with 4 food options and prices:
# Pizza - $15.99
# Burger - $12.50
# Salad - $9.99
# Pasta - $13.75
# Ask user to choose by number (1-4)
# Ask if they want a drink (+$2.50)
# Calculate total with 8% tax
# Display itemized bill
# Create file: question2.py
# Example Output:


# === YOUR ORDER ===
# Food: Pizza - $15.99
# Drink: Yes - $2.50
# Subtotal: $18.49
# Tax (8%): $1.48
# Total: $19.97



print("=== MENU ===")

print("1. Pizza - $15.99")
print("2. Burger - $12.50")
print("3. Pizza - $9.99")
print("4. Pizza - $13.75\n")

choice = int(input("Please selecet between (1-4) "))



if choice == 1 :
  cost = 15.99
  food = print(f"Food: Pizza - $15.99")
elif choice == 2 :
  cost = 12.50
  food = print(f"Food: Burger - $12.50")
elif choice == 3 :
  cost = 9.99
  food = print(f"Food: Salad - $9.99")
elif choice == 4 :
  cost = 13.75
  food = print("Pasta - $13.75")
else:
  print(f"Please select betweeen 1-4")


drink = input("Woul you like a drink? ($2.50) (yes/no): ")
subtotal = cost + 2.50
tax = .08
cost = subtotal + tax

print("===Your Order===\n")
if drink =="yes" :
  print(f"Food: {food}")
  print(f"Drink: Yes - $2.50")
  print(f"Tax (8%): ${((subtotal) * .08):.2f}")
  print(f"Subtotal: ${(cost + 2.50)}")
  
  print(f"Total: {(cost + tax) * tax:.2f}")



