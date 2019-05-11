n=int(input("Enter how many numbers:")) 
m=int(input("Enter the num:")) 
l=[]
c=0
for i in range(n): 
    num=int(input("Enter the n:")) 
    l.append(num) 
for x in l: 
    if(x==m): 
        c=c+1
if(c==0): 
    print("no") 
else: 
    print("yes") 
