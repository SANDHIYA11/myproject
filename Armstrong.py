Ll=int(input("Enter the limit:")) 
Ul=int(input("Enter the limit:")) 
for num in range (Ll, Ul+1): 
sum=0
temp=num
while temp>0: 
digit=temp℅10
sum+=digit**3
temp//=10
if num==sum: 
print(num) 
