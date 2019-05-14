s=input("Enter the string:")
n=int(input("Enter the number:"))
l=len(s)
j=l-n
lst=list(s)
str=""
for i in range(j):
  q=lst[j:]
for i in q:
  str=str+i
print(str)
