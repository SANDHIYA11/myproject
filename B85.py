n=input("Enter the string:")
l=len(n)
even=[]
odd=[]
g=[]
h=[]
st=""
st1=""
for l in range(l):
  if(l%2!=0):
    odd.append(l)
  else:
    even.append(l)
for i in even:
  g.append(n[i])
for z in g:
  st=st+z
for j in odd:
  h.append(n[j])
for x in h:
  st1=st1+x
print(st,st1)
