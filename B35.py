n=input("Enter the sentence:")
count=0
for i in n:
  if(i.isdigit()):
    count=count+1
  else:
    count=0
print(count)
