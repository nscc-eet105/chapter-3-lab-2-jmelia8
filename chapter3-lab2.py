#Joe Melia EET-107

print("Jane's Stuff Store\n")

items = int(input("How many items would you like to purchase: "))
total = 0
for item in range(items):
    cost = float(input("Enter the price of item " + str(item +1) + ": "))
    total = total + cost
average = total / items
print("\nThe total cost of your meal is $", total)
print("The average cost of each item is $", average)

