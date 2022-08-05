# I created the age variable using the input() function
age = input("What is your current age?")

# I converted age to an int
age_as_int = int(age)

# creating a variable for days, weeks and months
years = 90 - age_as_int
days = years * 365
weeks = years * 52
months = years * 12

#Using f-string
print(f"You have {days} days, {weeks} weeks, and {months} months left")
