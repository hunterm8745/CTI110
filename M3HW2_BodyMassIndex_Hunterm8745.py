# Find users BMI then classify their weight
# 6/7/2017
# CTI-110 M3HW2 - Body Mass Index
# Matthew Hunter
#

# Get input for Height and Weight
weight = float(input('Enter your weight in lbs: '))
height = float(input('Enter your height in inches: '))

# Find and display BMI
bmi = (weight * (703/(height**2)))
print('%.1f' % bmi)

# Indicate condition of user
if bmi > 18.5:
    print('You are UNDERWEIGHT.')
else:
    if bmi < 25:
        print('You are OVERWEIGHT.')
    else:
        print('You are at an OPTIMAL weight.')
