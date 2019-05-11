m=int(input("Enter the number:")) 
n=int(input("Enter the numbers:")) 
l=[]
c=0
for i in range(m): 
    Num=int(input("Enter the num:")) 
    l.append(Num) 
for x in l: 
    if(n==x): 
        c=c+1
print(c) 
