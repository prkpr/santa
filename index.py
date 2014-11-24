# Open file read line N, put in array till file is empty
# After reading line, 2 arrays
# Map one Fi to a Mi and let the value update to remove that Mi from the group to be sorted
# Map one M to a F and let the value update to remove that Fi from the group to be sorted
# duplicate arrays, generate a random number, choose a girl from first array 
# if gender is same, choose again
# if gender is different,send email
# complete till end of array
# Give an output

#fobj_persondata = open('Santa.txt','r')

#with open('Santa.txt') as fobj_persondata:
#	for line in fobj_persondata:
#		print line

List = open("Santa.txt").readlines()

print List[0]

for element in List:
	persondata = element.split()
	print persondata[1] # Name is printed at every even number and Gender is printed at every odd number

    


