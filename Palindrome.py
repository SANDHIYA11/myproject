A=int(input("Enter a number:")) 
Temp=A
Rev=0
while(A>0): 
Dig=A℅10
Rev=Rev*10+Dig
A=A//10
if(Temp==Rev): 
print("The number is palindrome") 
else:
print("The number is not a palindrome") 
