# calculate calories burned at set increments of time
# 6/14/2017
# CTI-110 M4HW1 - Calories Burned
# Matthew Hunter
#

calPerMin = 4.2

for num in range(31):
    if num == 10 or num == 15 or num == 20 or num ==25 or num == 30:
        burned = calPerMin * num
        print(num,'minutes: %.2f calories' % burned)
