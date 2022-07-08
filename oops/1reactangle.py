#1.what is a class
"""
"""
#2.what is __init__ methos
#3.whats is funtion
#4.define while loop
#5.how to call object 
#6.define self :
"""self is keyword to define an instance or an object of the
the class and it is a first perameter of the class the method and attributes
 of the class form its local variables."""

class rectangle():
	def __init__(self,breath,length):
		self.breath=breath
		self.length=length
	def area(self):
		return self.length*self.breath
while True:		
	a=int(input("Enter the length of rectangle:"))
	b=int(input("Enter the breath of rectangle:"))
	obj=rectangle(a,b)
	print("area of the rectangle:",obj.area())		

		