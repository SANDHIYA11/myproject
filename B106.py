n=int(input("Enter the count:"))
pos=int(input("Enter the position:"))
l=[]
for i in range(n):
  num=int(input("Enter the number:"))
  l.append(num)
element=l[pos-1]
print(element)
