from math import sqrt
from sys import maxint
import copy

citycount = 0
cities = {}
shortestdistance = maxint
shortestpermuation = []

def combi(xs, low=0):
	if low + 1 >= len(xs):
            yield xs
	else:
		for p in combi(xs, low + 1):
			yield p        
		for i in range(low + 1, len(xs)):
			xs[low], xs[i] = xs[i], xs[low]
			for p in combi(xs, low + 1):
				yield p
			xs[low], xs[i] = xs[i], xs[low]
	
def distance_math(one, two):
	x = sqrt((int(two[0]) - int(one[0]))**2 + (int(two[1]) - int(one[1]))**2)
	return x

f = raw_input("enter filename: ")
file = open(f, 'r')
for line in file:
	words = line.split()
	if words[0] == 'DIMENSION:':
		citycount = int(words[1])
	if words[0].isdigit():
		#print words
		x = [int(words[1]), int(words[2])]
		cities[int(words[0])] = x
	else:
		pass

for p in combi([x+1 for x in range(citycount)]):
	trip_distance = 0
	for i in range(1, len(p)-1):
		if (i+1 % len(p)+1) == 0:
			j = 1
		else:
			j = i+1
		#print i, j
		distance = distance_math(cities[p[i]], cities[p[j]])
		trip_distance = trip_distance + distance
	if trip_distance < shortestdistance:
		print trip_distance, shortestdistance
		shortestdistance = trip_distance
		print p
		shortestpermuation = copy.deepcopy(p)
		
print shortestpermuation
print shortestdistance