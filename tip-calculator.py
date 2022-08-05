# If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 

print ("Welcome To My Tip Calculator!")

total_bill = int(input("What is the total bill? /n"))

number_friends = int(input("What is the total number of friends/n"))

tip_percentage = int(input("What is the tip percentage?/n"))


payment_division = (total_bill * (1+ tip_percentage/100)) / number_friends

print(f"Each person should pay: ${round(payment_division, 2)}")
