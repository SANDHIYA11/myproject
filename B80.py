l=[]
n=int(input("Enter the number:"))
for i in range(n):
  num=int(input("Enter the num:"))
  l.append(num)
for x in l:
  if(x%2!=0):
    print(x)
