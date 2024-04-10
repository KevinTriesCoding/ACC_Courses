#Kevin Moye, Complete
# This program takes the input of 5 critic reviews for a restaurant and averages them out into one score.
# The average score is then processed into a star rating equivalent in a range of 0 - 5 stars.

TOTAL_CRITICS = 5

def main():
# main function to loop through 5 critic reviews and get the average of them
# function then takes average and passes it through determine_stars for processing
    composite_score = 0
    
    #while loop to include input validation so that 5 valid inputs are required to continue program
    critic_count = TOTAL_CRITICS
    while critic_count != 0:
        critic_input = int(input("Please enter critics score between 0 and 10: "))
        if 0 <= critic_input <= 10:
            composite_score += critic_input
            critic_count -= 1
        else:
            print ("Error: An integer between 0 and 10 was not entered. Please try again. ")
    
    average_score = composite_score / TOTAL_CRITICS
    determine_stars(average_score)


def determine_stars(average_score):
#function to process the average score into its equivalent star rating
    if average_score >= 9:
        print (f"Your score of {average_score} gives you *****")
    elif 8.0 <= average_score <= 8.9:
        print (f"Your score of {average_score} gives you ****")
    elif 7.0 <= average_score <= 7.9:
        print (f"Your score of {average_score} gives you ***")
    elif 6.0 <= average_score <= 6.9:
        print (f"Your score of {average_score} gives you **")
    elif 5.0 <= average_score <= 5.9:
        print (f"Your score of {average_score} gives you *")
    else:
        print (f"Your score of {average_score} gives you No stars") 

main()