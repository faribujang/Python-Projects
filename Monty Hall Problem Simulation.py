# Simulate the Monty Hall Problem used in game shows

import random

stay = 0	# Amount of times "Stay" won out of 1000 rounds
switch = 0	# Amount of times "Switch" won out of 1000 rounds

for i in range(1000):	# 1000 simulated rounds

    prize = 1			# Give different values to each option
    zonk = 0

    doors = [prize, zonk, zonk]	# Possible doors to choose
    random.shuffle(doors)

    ran = random.randrange(3)	# Randomly choose one of 3 doors

    user = doors[ran]			# Storing random guess

    del (doors[ran])			# Deleting random guess

    huh = zonk
    for x in doors:
        if x == zonk:
            del (doors[huh])	# Deletes "zonk" when it finds it
            break
        huh += 1				# Add one "zonk" back

    if user == prize:			# If winner is "stay", add one to "stay" wins
        stay += 1

    if doors[0] == prize:		# If winner is "switch", add one to "switch" wins
        switch += 1


stay_percent_won = (stay / (stay + switch)) * 100	# Percentage of "Stay" wins

switch_percent_won = (switch / (stay + switch)) * 100	# Percentage of "Switch" wins


print("Stay =", stay)
print("Switch =", switch)

print("Stay Percent Won =", stay_percent_won, "%")
print("Switch Percent Won =", switch_percent_won, "%")
