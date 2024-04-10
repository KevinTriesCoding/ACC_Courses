
#Prompts for the users high and low numbers
user_low_num = int(input("Please select a number: "))
user_high_num = int(input("Please select another number that is greater than your first: "))

#initialize variable to get total of each iteration "e.g. 5! = 1 + 2 + 3 + 4 + 5 = 15"
total = 0

#For loop that sets the the first input as the lower bound and second as the upper bound and iterates through the range by 1
# + 1 added to ensure that it stops at user_high_num exactly!
for iteration in range (user_low_num, user_high_num + 1, 1):
    iteration_multiple = iteration * 10
    print (f"{iteration}\t{iteration_multiple}")

#
for iteration in range (user_low_num, user_high_num + 1, 1):
    total += iteration

print (f"The sum of the range you chose is {total}")