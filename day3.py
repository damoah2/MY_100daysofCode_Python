#Date 11/14/2020
#Project from Udemy Course


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

#ask user weather if they want to go left or right
step1 = input('Do you want to go left or right?\n')
#If they choose right
if step1.lower() == 'right':
    #they will fall in to a holo and that is GAME OVER
    print('Oh no, you fell into a hole. GAME OVER!!!')
#else if the user choose to go left
elif step1.lower() == 'left':
    print('Congrats, you made the right choice, on to the next step.')
    print('While walking down a road you came upon a road block.')
    print('''To your left there is a river, that you can swim across to get
to the other side and continue your journey.''')
    print('You can wait for the road block to be move or you can swim.')
    #ask them if they want to swim or wait\
    choice = input('Do you want to swim or wait?\n')
    #if the user choose to swim or do anything also else
    if choice.lower() == 'swim':
        #the user will be attacted by trout. GAME OVER
        print('Attacted by trout. GAME OVER!!!')
    #else if the user choose to wait
    elif choice.lower() == 'wait':
        print('Congrats, you made the right choice, on to the next step.')
        print('You arrival in right of building.')
        print('The building has 3 doors; red, yellow, and blue.')
        #ask them which door to pick
        door_color = input('Which door? red, yellow or blue\n')
        #if the door they pick is Red
        if door_color.lower() == 'red':
            #the user is Burned by fire. GAME OVER
            print('Burned by fire. GAME OVER!!!')
        #else if the door they pick is Yellow
        elif door_color.lower() == 'yellow':
            #the user Wins the game. WINNER
            print('YOU ARE THE WINNER!!!')
        #else if the door they pick is Blue
        elif door_color.lower() == 'blue':
            #the user is eaten by beasts. GAME OVER
            print('Eaten by beasts. GAME OVER')
        #anything else
        else:
            #GAME OVER
            print('GAME OVER')
