# Kevin Moye, complete
# This is a program that calculates the discounted price of a software order based on the
# quanitity of products purchased

#variables for quantity, total, and discounts to set up logic tree
amount_purchased = int(input("How many software packages did you purchase: "))

discount_10 = 49
discount_20 = 99
discount_30 = 149
discount_40 = 150

total_price = 149 * amount_purchased
discounted_total = amount_purchased

#logic tree for discounts based on amount purchased 
if 10 <= amount_purchased <= discount_10:
    discounted_total = total_price - (total_price * .10)

elif amount_purchased <= discount_20:
    discounted_total = total_price - (total_price * .20)

elif amount_purchased <= discount_30:
    discounted_total = total_price - (total_price * .30)

elif amount_purchased >= discount_40:
    discounted_total = total_price - (total_price * .40)

else:
    discounted_total = total_price

#print statement to display total after discount applied
print (f'Your total price is {discounted_total}')
