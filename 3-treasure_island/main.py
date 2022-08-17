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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 

direction = input("You are standing on the rails of the third mainland bridge")

#writing the conditional statements. New knowledge, if you don't want python to ask you
#to assign a variable to left or any other thing listed, wrap it in quotation marks. As seen below.

if direction == "left":
    wait_or_swim = input("You have fallen into the atlantic ocean")
elif direction == "right":
    print("You've been crushed by a danfo. Game Over!")
else:
    print("You chose an option that doesn\'t exist")

if wait_or_swim == "wait":
    color = input("You arrived at ebutte metta unharmed.")
elif wait_or_swim == "swim":
    print("You have been eaten by a shark.\nGame Over.")
else:
    print("You chose an option that does not exist.")

if color == "red":
    print("You fell into a room full of fire.\nGame Over.")

elif color == "green":
    print("Congratulations, you have found the treasure!")

elif color == "blue":
    print("You fell into a ditch.\nGame Over.")

else:
    print("You chose a door that does not exist.\nGame Over.")
