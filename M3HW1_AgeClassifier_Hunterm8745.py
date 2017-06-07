# Classify a person based on their age
# 6/7/2017
# CTI-110 M3HW1 - Age Classifier
# Matthew Hunter
#

# Get input for age
age = float(input('Enter Age in Years: '))

# Determine classification
if age <= 1:
    print('That person is an infant.')
else:
    if age < 13:
        print('That person is a child.')
    else:
        if age < 20:
            print('That person is a teenager.')
        else:
            print('That person is an Adult.')
