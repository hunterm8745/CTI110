# Use two functions to calculate the average of 5 tests and determine the
# the grade of each one
# 6/19/2017
# CTI-110 M5T1_KilometerConverter 
# Matthew Hunter
#

def main():
    calc_average()

def calc_average():
    
    average = 0
    
    for x in range(1, 6):
        grade = float(input('Enter Test grade: '))
        determine_grade(grade)
        average += grade

    average /= 5

    print()
    print('The average of the grades is', average)
    determine_grade(average)

def determine_grade(num):

    grade_A = 90
    grade_B = 80
    grade_C = 70
    grade_D = 60
    
    if num >= grade_A:
        print('The grade is A.')
    elif num >= grade_B:
        print('The grade is B.')
    elif num >= grade_C:
        print('The grade is C.')
    elif num >= grade_D:
        print('The grade is D.')
    else:
        print('The grade is F.')
        

main()
    
