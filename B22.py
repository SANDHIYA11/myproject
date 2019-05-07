from array import *
x=array('i', []) 
a=int(input("Enter the number:")) 
for i in range(a): 
   n=int(input("Enter the numbers:")) 
   x.append(n) 
print("The maximum number is:",max(x)) 

