# If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

#Write your code below this line 

print ("Welcome To My Tip Calculator!")

# I created a variable for the bill using the input function, then converted it to a float function.
total_bill = float(input("What is the total bill? $"))

# made a variable asking for the number of friends, I also converted the value to an int.
number_friends = int(input("What is the total number of friends?"))

#I created a variable using the input function asking for the percentage of the tip
tip_percentage = int(input("What is the tip percentage? 10, 12 or 15? "))

# this variable mutiplies the total bill with the tip percentage divided by the number of friends.
#firstly, using PEMDAS LR, divide the tip_percentage by 100 and add 1 to it
#then multiply the value by the total bill divided by the number_friends
payment_division = (total_bill * (1 + tip_percentage/100)) / number_friends

#here we are rounding the total value to two. I used the f-string and round() function
print(f"Each person should pay: ${round(payment_division, 2)}")


#another method to divide the payment
#tip_percentage = tip / 100
#total_tip_amount = total_bill * tip_percentage
#total_bill = toatl_bill + total_tip_amount
#bill_per_person = total_bill / number_friends
#final_amount = round(number_friends, 2)
