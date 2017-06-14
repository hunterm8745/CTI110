# Calculate pay for worker using exponential pennies
# 6/14/2017
# CTI-110 M4HW2 - Pennies for Pay 
# Matthew Hunter
#

day = 1
penny = 1
totalPay = 0

days = int(input('How many days did you work?: '))

while days < 1:
    print('You need to have worked at least 1 day.')
    days = int(input('How many days did you work?: '))

print('Days worke\tMoney made')
print('--------------------------')

for day in range(0, days):
    print(day, '\t\t', penny)
    penny *= 2
    totalPay += penny

print('total: $', (totalPay / 100))

