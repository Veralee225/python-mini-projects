# Instructions

You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

`number of cans = (wall height ✖️ wall width) ÷ coverage per can`

e.g. `Height = 2, Width = 4, Coverage = 5`

`number of cans = (2 ✖️ 4) ÷ 5`

                     = 1.6

But because you can't buy *0.6* of a can of paint, the result should be rounded up to 2 cans.

IMPORTANT: Notice the name of the function and parameters must match those on line *13* for the code to work.

## Example Input

test_h = 3
test_w = 9
Example Output
You'll need 6 cans of paint.

## Hint

- 1. To round up a number:

[Stackoverflow](https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python)

- 2. Make sure you name your function/parameters the same as when it's called on the last line of code.

## Test Your Code

Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.

[Solution](https://repl.it/@appbrewery/day-8-1-solution)



# Prime Checker Exercise

## Instructions

Prime numbers are numbers that can only be cleanly divided by *themselves* and *1*.

[Wikipedia](https://en.wikipedia.org/wiki/Prime_number)

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. *2* is a prime number because it's only divisible by *1* and *2*.

But *4* is not a prime number because you can divide it by *1*, *2* or *4*.

Here are the numbers up to *100*, prime numbers are highlighted in yellow:

### Example Input 1

`73`

### Example Output 1

*It's a prime number.*

### Example Input 2

`75`

### Example Output 2

It's not a prime number.

### Hint

### Remember the modulus

[Stack Overflow](https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python)

Make sure you name your function/parameters the same as when it's called on the last line of code.

Use the same wording as the Example Outputs to make sure the tests pass.

[Solution](https://repl.it/@appbrewery/day-8-2-solution)
