#!/usr/bin/python 2.7

# If we list all the natural numbers
# below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 
# below 1000.

counter = 0 
terminating_condition = 1000
sum_of_multiples = 0 

while counter < terminating_condition:
	if counter % 3 == 0 and counter % 5 == 0: 
		sum_of_multiples += counter
	elif counter % 3 == 0:
		sum_of_multiples += counter
	elif counter % 5 == 0: 
		sum_of_multiples += counter
	else: 
		sum_of_multiples += 0 
	counter += 1

print sum_of_multiples


