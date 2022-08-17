from secrets import choice


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to decision making.")
print("Your mission is to find something to eat or starve to death.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 

direction = input('You\'re standing at the edge of your door, caught between leaving you house or staying in. Where do you want to go? Type "left" or "right" \n')

#writing the conditional statements. New knowledge, if you don't want python to ask you
#to assign a variable to left or any other thing listed, wrap it in quotation marks. As seen below.

if direction == "left":

    level1 = input('You chose the chaotic world. There is a restuarant across the street. Type "wait" to wait for food. Type "walk" to keep moving. \n').lower()
    if level1 == "walk":
        choice = input('You arrived elm street unharmed. There is a building with three doors. One brown, one is ash, one black. Which color do you choose? \n').lower()
        if choice == "brown":
            print("It's a bar. Game Over.")
        elif choice == "ash":
            print("You pizza! You Win!")
        elif choice == "black":
            print("Your entered a gym. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You never find food. Game Over.")
else:
    print("You never left the doooor! It was all a dream. Game Over!")
