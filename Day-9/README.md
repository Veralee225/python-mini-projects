# Day 9

## Exercise 1

## Instructions

You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

- Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

- This is the scoring criteria:

- Scores 91 - 100: Grade = "Outstanding"

- Scores 81 - 90: Grade = "Exceeds Expectations"

- Scores 71 - 80: Grade = "Acceptable"

- Scores 70 or lower: Grade = "Fail"

## Expected Output

'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

## Hint
Remember that looping through a Dictionary will only give you the keys and not the values.


[Solution](https://repl.it/@appbrewery/day-9-1-solution)


## Exercise 2

## Instructions

- You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

- Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.

You've been to Moscow and Saint Petersburg.

DO NOT modify the travel_log directly. You need to create a function that modifies it.

## Hint

Look at the function call above to see what the name of the function should be.

The inputs for the function are positional arguments. The order is very important.

Feel free to choose your own parameter names.

[Solution](https://repl.it/@appbrewery/day-9-2-solution)
