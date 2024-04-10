# Kevin Moye
# Complete
# A program that calculates the monthly budget and expenses for a user. The program then takes the difference of the two and tells
# the user if they spent over or under they're planned budget



user_budget = int(input("Enter amount budgeted for the month: "))
user_continue = True
user_expense = 0
total_spent = 0

#while loop with nested if statement to continue/end program based on user input
while user_continue is True:
    user_expense = int(input("Enter an amount spent (enter 0 to quit): "))
    if user_expense != 0:
        total_spent += user_expense
        user_continue = True
    else:
        user_continue = False

budget_delta = user_budget - total_spent

print (f"Budgeted: {user_budget}")        
print (f"Spent {total_spent}")

#if/elif statements to print difference based on it being over/under/at budget
if budget_delta > 0:
    print (f"You saved {budget_delta}! Nice work!")
elif budget_delta < 0:
    budget_delta_positive = abs(budget_delta)
    print (f"You spent {budget_delta_positive} over your budget. Not good...")
elif budget_delta == 0:
   print (f"You spent exactly at your budget! Talk about good planning")