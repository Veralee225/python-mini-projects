# Head or Tail Exercise

head_tail.py

## Instructions
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for our testing code to check your work.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g. 1 means Heads 0 means Tails

## Example Output

*Heads*
or
*Tails*

## Test Your Code

Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.

[Solution](https://repl.it/@appbrewery/day-4-1-solution)

# Banker Roulette

# Main.py

## Instructions

You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

#### Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for our testing code to check your work.

## Example Input

Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

## Example Output
Michael is going to buy the meal today!

## Hint
You might need the help of the len() function.

[Link](https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list)

Remember that Lists start at index 0!

## Test Your Code
Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.

[Solution](https://repl.it/@appbrewery/day-4-2-solution)

# Treasure Map

## Instructions

You are going to write a program that will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what the nested list looks like:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

Now it looks a bit more like the coordinates of a real map:

Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical location and the second digit is the horizontal location. So an input of 23 should place an X at the position shown below:

First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "x". Remember that your nested list map actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].

## Example Input 1

column 2, row 3 would be entered as:
*23*

## Example Output 1

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']

## Example Input 2

column 3, row 1 would be entered as:

*31*

## Example Output 2

['⬜️', '⬜️', 'X']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']

## Hint

Remember that Lists start at index 0!
map is just a variable that contains a nested list. It's not related to the map function in Python.
 Remember that nested lists are accessed from out to in. So if list=[[A,B,C],[E,F,G]] then E = list[1][0]
Check that you haven't accidentally added extra spaces and the X is a capital X with a single quote around it. 
Correctly formatted:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']

*vs* 

Incorrectly formatted (missing a space before 'X and extra space after the X and extra space before the comma):

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️','X ' , '⬜️']

## Test Your Code

Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.

[Solution](https://repl.it/@appbrewery/day-4-3-solution)
