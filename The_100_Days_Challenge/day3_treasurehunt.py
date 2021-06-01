print(
    '''  
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
    '''
)

print('Your mission is to find the treasure')

direction = input('You\'re at a cross road. Where do youi want to go? Type "left" or "right" \n')

if direction == 'left':

    print('You ended on the never ending road')

    print('Game Over')

else:

    direction = input(
        'You come to cave entrance. It sounds like something big may live in there. Type "enter" or "turn around"\n')

    if direction == "enter":

        direction = input(
            'You find a dragon. He says "Bro, I am tired of watching this treasure, '
            'I want to fly around the world. Type "offer" to take the treasure of his hands. '
            'Type "deny" to not accept it\n')

        if direction == 'offer':

            print('Yay, you have the treasure and glory that comes with it.\nYou Win!')

        else:

            print('You left with nothing, but your pride. Congratulations!')

            print('Game Over')

    else:

        print('You never find the treasure')

        print('Game Over')
