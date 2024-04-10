
program_continue = True


while program_continue is True:
    # input variable for number 1 - 7
    number_selection = int(input("Please select a number between 1 and 7: "))
    
    # if, elif, else logic
    if number_selection == 1:
        print("You chose Monday")
        user_continue = input("Would you like to keep going (Y/N): ")
        if user_continue == "N":
            program_continue = False

        else:
            program_continue = True

    elif number_selection == 2:
        print("You chose Tuesday")
        user_continue = input("Would you like to keep going (Y/N): ")
        if user_continue == "N":
            program_continue = False

        else:
            program_continue = True

    elif number_selection == 3:
        print("You chose Wednesday")
        user_continue = input("Would you like to keep going (Y/N): ")
        if user_continue == "N":
            program_continue = False

        else:
            program_continue = True
    
    elif number_selection == 4:
        print("You chose Thursday")
        user_continue = input("Would you like to keep going (Y/N): ")
        if user_continue == "N":
            program_continue = False

        else:
           program_continue = True

    elif number_selection == 5:
        print("You chose Friday")
        user_continue = input("Would you like to keep going (Y/N): ")
        if user_continue == "N":
           program_continue = False

        else:
            program_continue = True

    elif number_selection == 6:
        print("You chose Saturday")
        user_continue = input("Would you like to keep going (Y/N): ")
        if user_continue == "N":
            program_continue = False

        else:
            program_continue = True

    elif number_selection == 7:
        print("You chose the Sunday")
        user_continue = input("Would you like to keep going (Y/N): ")
        if user_continue == "N":
            program_continue = False

        else:
            program_continue = True

    else:
        print("You did not choose a number between 1 and 7. Please try again.")
        user_continue = input("Would you like to keep going (Y/N): ")
        if user_continue == "N":
            program_continue = False

        else:
            program_continue = True