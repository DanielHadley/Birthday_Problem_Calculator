# Simulate the birthday problem for n number of people


import random
 
year = range(1,366)

def list_of_birthdays(numberPeople): 
	birthdays = []
	for i in range(0,numberPeople):
		i = random.choice(year)
		birthdays.append(i)
	return birthdays

def at_least_two_share(numberPeople):
	shared = len(list_of_birthdays(numberPeople)) - len(set(list_of_birthdays(numberPeople)))
	if shared > 0:
		return True
	else:
		return False

def prob_of_shared(numberPeople, numSims):
	shares = 0
	for i in range(0,numSims):
		success = at_least_two_share(numberPeople)
		if success == True:
			shares += 1
	return (float(shares) / numSims)

print '{:.2%}'.format(prob_of_shared(60, 1000))

# We have the same birthday, your husband shares a bday with my twins (today) and I'm pretty sure my son shares a Bday with your twins???

def three_same_bdays():
	myFamily = sorted(list_of_birthdays(3))
	herFamily = sorted(list_of_birthdays(3))
	if myFamily == herFamily:
		return True
	else:
		return False


def number_of_three_shared(numSims):
	shares = 0
	for i in range(0,numSims):
		success = three_same_bdays()
		if success == True:
			shares += 1
	return shares

print number_of_three_shared(10000000)


