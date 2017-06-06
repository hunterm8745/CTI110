# Calculate total amount of a meal at a restaurant
# 6/6/2017
# CTI-110 M2HW2 - Tip Tax Total
# Matthew Hunter
#

charge = float(input('Charge for meal: $'))


tip = float(charge * .18)
tax = float(charge * .07)

print('Tip = $%.2f' % tip)
print('Tax = $%.2f' % tax)
print('Total = $%.2f' % (charge + tip + tax))
