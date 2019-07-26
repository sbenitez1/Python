##################################################
## {Code for learning Python - First steps}
##################################################
## Author: {Sandra Benitez Pena}
## Email: {sbenitez1@us.es}
## Date:  {2019-07-26}
##################################################

# Outline
#------------------
# 1. Variable and list (simple data) creation
# 2. Treatment of variables
# 3. Treatment of list
#		3.1. Basic attributes of lists - accessing to elements
#		3.2. Modifying and copying lists, and how the modification affects to copies
#		3.3. Adding elements to lists
#		3.4. Removal of elements in a list
#       3.5. Other operations in a list
# 4. Basic operations as calculator
#-------------------



# Variable and list (simple data) creation
#-------------------------------------------

a = 3				#Here we create variable "a", set equal to 3
b = [1,2,3,4,5]		#Here we create list "b", containing values from 1 to 5

print(a)			#Show "a"
print(b)			#Show "b"



# Treatment of variables
#-------------------------------------------

c = 3 + 5			#As every programming language, Python can be used as a calculator       
print(c)			#Show "c"
print(4 + 6)        #We can also show the result of an operation without assignation

d = c               #We can copy the value of a variable

c = 7               #And, if we change the value of the variable...
print(c)            #We see that it changes!
print(d)            #While "d" maintains the "original" value of "c"

C = 2				#Even if...
C = 5               #We declare it as a "constant" as we would do in other programming languages
                    #(note: in other languages, declaring a constant with capital letter would make
					#print(C) equal to 2. That is to say: the value cannot be changed to 5!)
print(C)            #We see how we obtain 5 instead of 2 ("constants" doesn't exist in Python...)



# Treatment of list
#-------------------------------------------


#Basic attributes of lists - accessing to elements

print(len(b))              #"len" give us the lenght of a list
print(b[0])                #lists starts with index "0"
print(b[4])                #Hence, finish with index "len(b)-1"

# Modifying and copying lists, and how the modification affects to copies

b2 = b                     #There are many ways to copy the lists...
import copy                #This library will be necessary for more "complex" list copies
b3 = copy.copy(b)          #Shallow copy
b4 = copy.deepcopy(b)      #Deep (recursive) copy

print(b)					#Show "b"
print(b2)					#Show "b2"
print(b3)					#Show "b3"
print(b4)					#Show "b4"

b[0] = "change"             #Change value of "b[0]"
print(b)					#Show "b" - It has changed
print(b2)					#Show "b2" - It has changed
print(b3)					#Show "b3" - It has NOT changed
print(b4)					#Show "b4" - It has NOT changed

bComplex = [[1,"Hello",3],["a",1]]       #Create a more "complex" list
bComplex2 = bComplex                     #Copy the list
bComplex3 = copy.copy(bComplex)          #Shallow copy
bComplex4 = copy.deepcopy(bComplex)      #Deep (recursive) copy

print(bComplex)						#Show "bComplex"
print(bComplex2)					#Show "bComplex2"
print(bComplex3)					#Show "bComplex3"
print(bComplex4)					#Show "bComplex4"

bComplex[0][0] = "change"   		#Change value of "bComplex[0][0]"
print(bComplex)						#Show "bComplex" - It has changed
print(bComplex2)					#Show "bComplex2" - It has changed
print(bComplex3)					#Show "bComplex3" - It has changed
print(bComplex4)					#Show "bComplex4" - It has NOT changed


# Adding elements to lists

addingList = []						#We create a new list
print(addingList)					#And show it - it is empty ([])

addingList.append(1)                #Insert "1" to list
print(addingList)					#And show it - [1]

addingList.append(2)                #Insert "2" to list					
addingList.append(4)                #Insert "4" to list
print(addingList)					#And show it - [1,2,4]

addingSuperList = []				#We create a new "superlist" - it will contain 
									#the previous list
print(addingSuperList)				#And show it - it is empty ([])

addingSuperList.append(addingList) 	#Insert prevoius list - now, we have a list of lists!
print(addingSuperList)				#And show it [[1,2,4]] (note the double square bracket)

addingSuperList.append(bComplex[0]) #Insert the first list in "bComplex"
print(addingSuperList)				#And show it

addingSuperList.append("Add") 		#Insert "Add" string to the list
print(addingSuperList)				#And show it



# Removal of elements in a list 

removingList = [0,1,2,3,4,5,6,7,8,9,10]		#We create a new list
print(removingList)							#And show it

removingList.remove(5) 						#We remove, if exists, the first element equal to the selected (5)
removingList.remove(6)   					#We remove, if exists, the first element equal to the selected (6)
print(removingList) 						#And show it

removingList.pop() 							#We remove the last element
print(removingList)							#And show it

removingList.pop(2) 						#We remove, if exists, the element the selected index 
											#(2nd element - remember, starting in the 0th)
print(removingList) 						#And show it

removingList2 = ['G','E','E','K','S','F','O','R','G','E','E','K','S'] 		#We create a new list
print(removingList2)														#And show it

Sliced_removingList2 = removingList2[3:8]                                   #And only remain (starting in 0, 
																			#remember), from the 3rd to the (8-1)th
																			#element
print(Sliced_removingList2) 												#And show it
  
Sliced_removingList2 = removingList2[:-6] 	#We remove from the sixth element, remaining it (and starting in 0th)
print(Sliced_removingList2) 				#And show it
  
Sliced_removingList2 = removingList2[5:] 	#We remove up to the 5th element, remaining it (and starting in 0th)
print(Sliced_removingList2)  				#And show it
  
  
  
# Other operations in a list

list = ['G',1,'E',3,10,'F','O',2,'G','E',5,'K','S']	#We create a new list
Sliced_list = list[:]  								#We "copy" the list in the same order
print(Sliced_list)   								#And show it
  
Sliced_list = list[::-1] 							#We "copy" the list in the reverse order
print(Sliced_list)   								#And show it

list2 = [0,1,2,3,4,5,6,7,8,9,10]		#We create a new list
maximumOfList = max(list2)				#We calculate the maximum
print(maximumOfList)					#And show it

minimumOfList = min(list2)				#We calculate the minimum
print(minimumOfList)					#And show it

sumOfList = sum(list2)					#We calculate the minimum
print(sumOfList)						#And show it



# Basic operations as calculator
#-------------------------------------------

print(3+4)					#Show addition
print(3-4)					#Show subtraction
print(3*4)					#Show multiplication
print(3/4)					#Show division (see note below, please (*))
print(3//4)					#Show floor division (e.g. 5//2 = 2)
print(4%3)					#Show modulo (4%3 = 4 mod 3)
print(-3)					#Show "negative"
print(abs(-3))				#Show absolute value
print(3^4)					#Show exponent (v1)
print(3**4)					#Show addition (v2)
import math					#This library will be necessary for more "complex" operations
print(math.exp(3))			#Show exponential in base "e"
print(math.sqrt(3))         #Show squared root
print(round(13.176945,3))   #We round up to 3 decimal digits

print(0.6/0.2)				#(*) Beware that due to the limitations of floating point arithmetic, 
							#rounding errors can cause unexpected results.
print(0.6//0.2)



