# Display the numbers in file from homework 1, and show how many
# lines there are and the total of all numbers in the file
# 6/22/2017
# CTI-110 M6HW2 - Random Number File Reader
# Matthew Hunter
#

def main():
    lines = 0
    total = 0

    try:
        infile = open('numbers1.txt', 'r')

        for line in infile:
            print(line)
            lines += 1
            total += int(line)

    except:
        print('An error occured')

    print(lines)
    print(total)

main()
