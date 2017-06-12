# Corrected errors in Workbench problem #4, page 115
# 6/7/2017
# CTI-110 M3LAB - Debugging
# Matthew Hunter
#

# Create Main function to call later
def main():
    A_score = 90    # Set lowest score for A
    B_score = 80    # Set lowest score for B
    C_score = 70    # Set lowest score for C
    D_score = 60    # Set lowest score for D
                    # Anything lower is F
    
    # Have user enter their score
    score = float(input('Enter your Score: '))

    # Use if-elif-else to compair and determine grade
    if score >= A_score:
        print('Your grade is A.')
    elif score >= B_score:
        print('Your grade is B.')
    elif score >= C_score:
        print('Your grade is C.')
    elif score >= D_score:
        print('Your grade is D.')
    else:
        print('Your grade is F.')

# Call Main function
main()
