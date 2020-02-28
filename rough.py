# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])
# ------------+++++++++++++-------------
for i in genre:
	print ('I hate',i)
# ------------+++++++++++++-------------
j = 0
sum = 0
x = list()
for k in range(1,50):
	sum = k*k
	x.append(sum)
print ('List :',x)

print ('Put more concentration in learning python')
