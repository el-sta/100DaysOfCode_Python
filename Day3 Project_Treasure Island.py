#Day3 Project: Treasure Island

# art from page https://ascii.co.uk/art

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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")
print("Your at a cross road. Where do you want to go?")
cross_road = input("Type left or right\n")
                   
if cross_road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    go_to_island = input("Type wait to wait for a boat. Type swim to swim across.\n")
    if go_to_island == "wait":
        print("You arrived at the island unharmed. There is a house with 3 doors.")
        print("One red, one yellow and one blue. Which door do you choose?")
        door = input("Type red, yellow or blue.\n")
        if door == "yellow":
            print("You win!")
        elif door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("ttached by troot. Game Over.")
else:
    print("You felt into a hole. Game Over.")
