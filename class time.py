class Time: 
def  init (self, hour, minute, second): 
self.hour = hour 
self.minute = minute 
self.second = second 
 
def   add  (self, other): 
totalhour = self.hour + other.hour 
totalminute = self.minute + other.minute 
totalsecond = self.second + other.second  
totalminute = totalminute + totalsecond // 60 
totalsecond = totalsecond % 60 
totalhour = totalhour + totalminute // 60 
totalminute = totalminute % 60 
return Time(totalhour,totalminute,totalsecond) 
def  repr (self): 
return(f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}') 
 
 
t1 = Time(11, 30, 49) 
t2 = Time(12, 48, 60) 
print(t1) 
print(t2) 
t3=t1+t2 
print("sum of time1 and time2:",t3)