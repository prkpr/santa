# Open file read line N, put in array till file is empty
# After reading line, 2 arrays
# Map one Fi to a Mi and let the value update to remove that Mi from the group to be sorted
# Map one M to a F and let the value update to remove that Fi from the group to be sorted
# duplicate arrays, generate a random number, choose a girl from first array 
# if gender is same, choose again
# if gender is different, send email
# complete till end of array
# Give an output

file = open('santa.txt', 'r')

contents = file.read()
santa_list = contents.split('\r') # creating list
banta_list = list(santa_list) # duplicating lists

import random

count = -1
index = -1

for i in santa_list:

	index += 1
	count += 2

	rand_gen = random.randrange(0, len(santa_list), 1)
	santa_chosen = santa_list[index]
	santa_chosen_name = santa_chosen.split()[0]
	santa_gender = santa_chosen.split()[1] #Trying to split each line into two parts and getting the second part from each line. How?
	number_boys = len(santa_gender)

	rand_gen1 = random.randrange(0, len(banta_list), 1)
	banta_chosen = banta_list[rand_gen1]
	banta_chosen_name = banta_chosen.split()[0]
	banta_gender = banta_chosen.split()[1]

	while (santa_chosen_name == banta_chosen_name):
		rand_gen = random.randrange(0, len(santa_list), 1)
		santa_chosen = santa_list[index]
		santa_chosen_name = santa_chosen.split()[0]

	banta_list.remove(banta_chosen)

	print santa_chosen_name, "will gift", banta_chosen_name, "!"

print number_boys
