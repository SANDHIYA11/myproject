N=int(input("Enter the number:")) 
Re=0
while(N>0): 
Dig=N℅10
Re=Re*10+Dig
N=N//10
print("reverse of number is:",Re) 
