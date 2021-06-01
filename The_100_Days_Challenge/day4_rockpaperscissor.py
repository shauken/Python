import random

myChoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

computerChoice = random.randint(0, 2)

rock = '''    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

rockpaperscissors = [rock, paper, scissors]

if myChoice >= 3 or myChoice < 0:

    print('You typed in invalid number, you lose!')

else:

    print(rockpaperscissors[myChoice])

    print('\nComputer chose:\n')

    print(rockpaperscissors[computerChoice])

    if myChoice == computerChoice:

        print('\nDraw\n')

    elif myChoice == 0 and computerChoice == 1:

        print('\nYou lose')

    elif myChoice == 0 and computerChoice == 2:

        print('\nYou Win')

    elif myChoice == 1 and computerChoice == 0:

        print('\nYou Win')

    elif myChoice == 1 and computerChoice == 2:

        print('\nYou Lose')

    elif myChoice == 2 and computerChoice == 0:

        print('\nYou Lose')

    elif myChoice == 2 and computerChoice == 1:

        print('\nYou Win')