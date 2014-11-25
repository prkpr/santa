file = open('santa.txt', 'r')

contents = file.read()
santa_list = contents.split('\r') # creating list
banta_list = list(santa_list) # duplicating lists

count = -1

for j in santa_list:
	count += 1
	index = -1
	for k in banta_list:
		index += 1
		person_data = santa_list[count]
		santa_gender = person_data.split()[1]
		person_data1 = banta_list[count]
		banta_gender = person_data1.split()[1] #now we have genders how do we stitch them with names? how to make the loop?

import random

index = -1

for i in santa_list:

	index += 1

	rand_gen = random.randrange(0, len(santa_list), 1) #I wanna know if we are getting one random number each time the loop runs or random number of random numbers in the range
	santa_chosen = santa_list[index]
	santa_chosen_name = santa_chosen.split()[0]

	rand_gen1 = random.randrange(0, len(banta_list), 1)
	banta_chosen = banta_list[rand_gen1]
	banta_chosen_name = banta_chosen.split()[0]

	while (santa_chosen_name == banta_chosen_name):
		rand_gen = random.randrange(0, len(santa_list), 1)
		santa_chosen = santa_list[index]
		santa_chosen_name = santa_chosen.split()[0]

	banta_list.remove(banta_chosen)

	print santa_chosen_name, "will gift", banta_chosen_name
