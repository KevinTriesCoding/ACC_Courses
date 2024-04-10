#while loop logic for user termination
user_continue = "Y"
while user_continue == "Y":
    
    #prompting user for two separate numbers
    user_num1 = int(input("Please enter a number: "))
    user_num2 = int(input("Please enter a second number: "))

    #numbers are added and printed
    num_sum = user_num1 + user_num2
    print (f"The sum of your two numbers is {num_sum}")

    #prompt user to terminate or continue program
    user_continue = input ("Would you like to continue (Y/N): ")