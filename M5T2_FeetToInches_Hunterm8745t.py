# Calculate how many inches are in an amount of feet
# 6/19/2017
# CTI-110 M5T2_FeetToInches 
# Matthew Hunter
#

def main():

    feet = int(input('Enter the number of feet: '))
    print()

    inches = feet_to_inches(feet)

    print('There are', inches, 'in', feet, 'feet.')

def feet_to_inches(num1):
    
    result = num1 * 12
    return result

main()
