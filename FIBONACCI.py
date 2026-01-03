n=int(input("Enter the number of terms:")) 
a=0 
b=1 
print("fibonacci series: \n",a,"\n",b) 
for i in range(1,n-1): 
c=a+b 
a=b 
b=c 
print(c)