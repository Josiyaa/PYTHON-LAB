class Publisher: 
def  init (self, pid, pname): 
self.publisher_id = pid 
self.publisher_name = pname 
 
class Book(Publisher): 
def  init (self, pid, pname, title, author): 
super(). init (pid, pname) 
self.title = title 
self.author = author 
class Python(Book): 
def  init (self, pid, pname, title, author, price, no_of_pages): 
super(). init (pid, pname, title, author) 
self.price = price 
self.no_of_pages = no_of_pages 
 
def display(self): 
print("Publisher ID:", self.publisher_id) 
print("Publisher Name:", self.publisher_name) 
print("Book Title:", self.title) 
print("Book Author:", self.author) 
print("Book Price:", self.price) 
print("Number of Pages:", self.no_of_pages) 
 
P1 = Python(101, "J.S Publications", "Wings of Fire", "A.P.J Abdul Kalam", 250, 300) 
P1.display()