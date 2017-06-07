# Find the area of two rectangles then find the larger one
# 6/7/2017
# CTI-110 M3T1 - Areas of Rectangles
# Matthew Hunter
#

# Receive input for rectangles
length1 = float(input('First Rectangles Length: '))
width1 = float(input('First Rectangles Width: '))
length2 = float(input('Second Rectangles Length: '))
width2 = float(input('Second Rectangles Width: '))

# Calculate area of rectangles
area1 = length1 * width1
area2 = length2 * width2

# Compare areas
if area1 != area2:
    if area1 > area2:
        print('The first rectangle has the larger area.')
    else:
        print('The second rectangle has the larger area.')
else:
    print('The two rectangles have the same area.')

