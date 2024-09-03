import random

#test_seed
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

# Checking for the length of the list
len_names = len(names)

# Variable to select a random person from the list
random_person = random.randint(0, len_names - 1)

# Printing the final result
print("Result is: \n")
print(f"{names[random_person]} will pay the bill today. Good luck {names[random_person]}. xD")
