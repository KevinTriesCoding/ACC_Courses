print ("Welcome to Python's Burgers. \nHow can we help you?")

burger_cost = int(input ("How much for a burger: "))
fries_cost = int(input ("How much for an order of fries: "))
shake_cost = int(input ("How much for a milkshake: "))

total_cost = burger_cost + fries_cost + shake_cost
average_cost = total_cost/3

print (f"Your total cost will be {total_cost}")
print (f"Your average cost at Python's Burgers will be: {average_cost}.\nThanks for stopping by!")