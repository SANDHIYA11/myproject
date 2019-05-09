n=input("Enter the number or character or special character:")
c=0
for i in n:
  if(i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*' or i=='(' or i==')' or i=='_' or i=='-' or i=='+' or i=='=' or i=='{' or i=='}' or i=='[' or i==']' or i=='|' or i=='\' or i==':' or i==';' or i=='"' or i==''' or i=='<' or i=='>' or i==',' or i=='.' or i=='?' or i=='/'):
    c=c+1
    print(c)
