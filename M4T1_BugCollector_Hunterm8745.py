# Use loop to calculate number of bugs caught over 5 days
# 6/14/2017
# CTI-110 M4T1 - Bug Collector
# Matthew Hunter
#

total = 0
day = 1

while day != 6:
    print('Day', day)
    bugs = int(input('How many bugs did the Bug Collector catch today?: '))
    total += bugs
    day += 1

print()
print('The Bug Collector caught', total, ' bugs over 5 days.')
