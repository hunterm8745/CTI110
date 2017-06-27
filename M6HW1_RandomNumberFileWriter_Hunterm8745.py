# Write an amount of psudorandom numbers to a file
# 6/21/2017
# CTI-110 M5T1 - File Display
# Matthew Hunter
#

def main():
    try:
        amount = int(input('How many numbers would you like to print? '))
    
        infile = open('numbers1.txt', 'w')

        for x in range (1, amount + 1):
            import random
            num = random.randint(1,500)
            num = str(num)

            infile.write(num + '\n')

            print(num)

        infile.close()

        print('Data writen to numbers1.txt')

    except:
        print('An error occured.')

main()
