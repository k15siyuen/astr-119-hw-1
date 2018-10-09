import numpy as np
import sys

#define a function that returns a value
def expo(x):
	return np.exp(x) #return the np e^x function
	
#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n): #i=[0,n-1]
		print (expo(float(i))) #call e^float(i)
		
#define a main function
def main():
	n = 10 #default value for n
	
	#check if there is command line argument
	#(so if n does not equal 10 you don't have to change the whole function)
	if(len(sys.argv)>1):
		n = int(sys.argv[1]) #if an argument was provided, use it for n
		
	show_expo(n) #call the expo subroutine
	
#run the main function
if __name__ == "__main__":
	main()