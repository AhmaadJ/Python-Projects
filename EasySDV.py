# Python code to demonstrate stdev() function 

# importing Statistics module 
import statistics 

# creating a simple data - set 
sample = [3.52, 2.02, 4.91, 3.22, 1.92] 

# Prints standard deviation 
# xbar is set to default value of 1 
print("Standard Deviation of sample is % s "
				% (statistics.stdev(sample))) 

#Prints the average
print()
print("Mean of the sample is :", statistics.mean(sample))