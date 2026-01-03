num1=int(input("Enter number1:")) 
num2=int(input("Enter number2:")) 
gcd=1 
n=min(num1,num2) 
for i in range(1,n): 
if((num1%i==0) and (num2%i==0)): 
gcd=i 
print("GCD of num1 and num2 is",gcd)