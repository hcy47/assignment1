



# Question 1: Movie Ticket Pricing (Lesson 1 - Variables & Output)
# Points: 8
# Write a Python program that calculates movie ticket costs with different pricing.
# Requirements:
# Ask the user for their name and age
# Set ticket prices: 
# Child (under 13): $8
# Adult(13−64):$12
# Senior (65+): $9
# Ask how many tickets they want (Ticket prices should be calculated based on the age of the person buying them)
# Calculate total cost and display a receipt-style output
# Use f-string formatting for the receipt
# Create file: question1.py


name = input("What is your name? ")
age = int(input("What is your age?\n "))


print('''===  Ticket Prices   ===''')
if age < 13:
  cost = 8
  ticket_info = "Child-($8.00)"

elif age <64:
  cost = 12
  ticket_info = "Adult-($12.00)"

else: 
  age > 65 
  cost = 9
  ticket_info = "Senior-($9.00)"

quantity = int(input("How many ticket would you want? "))
total = cost * quantity

print(  '''Ticket Summary''')
print(f'Name: {name}')
print(f"Age: {age}")
print(f'Ticket Quantity: {quantity}')
print(f"Ticket Info: {ticket_info}")
print(f"Your Total: {total} ")
print(f"Thanks for your purchase!")