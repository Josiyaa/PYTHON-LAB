def gcd(n1, n2): 
gcd = 1 
n = min(n1, n2) 
for i in range(1, n + 1): 
if (n1 % i == 0) and (n2 % i == 0): 
gcd = i 
print("GCD of n1 and n2 is", gcd) 
 
 
n1 = int(input("Enter first number: ")) 
n2 = int(input("Enter second number: ")) 
gcd(n1, n2)