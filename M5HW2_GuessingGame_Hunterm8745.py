# Generate a psudorandom number and have the user guess
# it untill they get it right
# 6/20/2017
# CTI-110 M5HW2 - Random Number Guessing Game
# Matthew Hunter
#

def main():
    random()


def random():
    import random
    choice = random.randint(1,100)
    game(choice)

def game(num):
    turns = 0

    print()
    guess = int(input("I'm thinking of a number between 1 and 100. What is it? "))

    while guess != num:
        if guess > num:
            guess = int(input('Too high. Try again. '))
            turns += 1
        elif guess < num:
            guess = int(input('Too low. Try again. '))
            turns += 1

    turns += 1

    print()
    print('Congratulations! That was right!')
    print('You used', turns, 'turn(s).')
    print()

    again = input('Play again? (Y/N) ')
    
    while guess == num:
        if again == 'y' or again == 'Y':
            main()
        elif again == 'n' or again == 'N':
            quit()
        else:
            again = input('Please enter Y or N.  ')

main()
                

