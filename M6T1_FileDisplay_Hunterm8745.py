# Open a file named numbers.txt and read contents
# 6/20/2017
# CTI-110 M6T1 - File Display
# Matthew Hunter
#

def main():
    try: 
        infile = open('numbers.txt', 'r')

        for line in infile:
            print(line)

        infile.close()
    except:
        print('An error occured.')

main()
