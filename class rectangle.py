class Rectangle: 
def  init (self,length,breadth): 
self. length=length 
self. breadth=breadth 
self.area=length*breadth 
def   lt  (self,other): 
return self.area<other.area 
r1=Rectangle(10,50) 
r2=Rectangle(15,25) 
if(r1<r2): 
print("First rectangle is smaller") 
elif(r1>r2): 
print("First rectangle is greater") 
else: 
print("Rectangles are equal") 
