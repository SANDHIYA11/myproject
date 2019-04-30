n=int(input("Enter the number:"))
a=0
for i in range(2,n//2+1):
  if(n%i==0):
    a=a+1
    if(a>=0):
      print("yes")
    else:
      print("no")
