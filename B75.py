s=input("Enter the sentence:")
lst=list(s)
l=len(s)
str=""
if(l%2!=0):
  q=l//2
  r=round(q)
  lst[r]="*"
  for j in lst:
    str=str+j
  print(str)
else:
  m=l//2
  j=m-1
  for i in range(j,m+1):
    lst[i]="*"
  for j in lst:
    str=str+j
  print(str)
