# Convert kilometers to miles
# 6/19/2017
# CTI-110 M5T1_KilometerConverter 
# Matthew Hunter
#

def main():
    kilometers = float(input('Enter number of kilometers: '))
    print()

    miles = kilometers * 0.6214

    print(kilometers, 'kilometers = %.2f miles' % miles)

main()
