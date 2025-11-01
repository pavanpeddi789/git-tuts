# programme for even or odd
num=56
if num%2==0:
    print("num is even")
else:
    print("num is odd")    
# program for divisible by 5 but not divisible by 10
num=35
if num%5==0 and num%10!=0:
    print("satisfy")
else:
    print("not satisfy")  
#biggest among two numbers
a=10
b=12
if a>b:
    print("a is greater")
else:
    print("b is greater")
#smallest among two numbers
a=12
b=15
if a<b:
    print("a is smaller")
else:
    print("b is smaller")  
#check is the number is divisible by 2 and 3 and 6
a=18
if a%2==0 and a%3==0 and a%6==0:
    print("satisfy with conditinos")
else:
    print("not satisfy")                 
# check if a person is eligible for vote
age=19
if age>18 :
    print("eligible to vote")
else:
    print("not eligible to vote")
# student is passed if all subjects is grester than 35    
m=36
s=38
sc=90
if m>=35 and s>=35 and sc>=35:
    print("student is passed")
else:
    print("not passed") 
#student pass atlest he got 35 in any one subject
m=36
s=25
sc=90       
if m>=35 or s>=35 or sc>=35:
    print("student is passed")
else:
    print("student is not passed")        
# student is passed if any two subjects is greater than 35 he is passed
m=45
s=45
sc=23
p_s=0
if m>=35:
    p_s+=1
if s>=35:
    p_s+=1
if sc>=35:
    p_s+=1
if p_s>=2:
    print("student is passed")
else:
    print("student is not passed")       
#biggest among three numbers
a=10
b=20
c=30
if a>=b and a>=c:
    print("a is greater")
elif b>=a and b>=c:
    print(" b is greater")
else:
    print("c is greater")  
# smallest among three numbers
a=10
b=20
c=30 
if a<b and a<c:
    print(" ais a smaller number")
elif b<a and b<c:
    print("b is smaller")
else:
    print(" c is smaller")                