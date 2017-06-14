# Calculate factorial of given number
# 6/14/2017
# CTI-110 M4HW3 - Factorial 
# Matthew Hunter
#

holder = 1
factorial = 1

num = int(input('Please enter a REAL number: '))

while holder < num:
    holder += 1
    factorial *= holder

print(factorial)
