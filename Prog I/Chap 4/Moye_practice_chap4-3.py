

#input statements for user integer and character
user_amount = int(input("Please select a positive integer that is less than or equal to 15: "))
user_char = input("Please select any character on your keyboard (just one please): ")

if user_amount > 15:
    print("You selected a value greater than 15 :(")

else:
    #for loop that iterates through a range from 1 - user_amount by +1
    #because it is a loop, the computer will keep each display for the square
    for integer in range (1, user_amount + 1, 1):

    #print statement takes user input and displayes it (user_amount) of times
        print (user_char * user_amount)