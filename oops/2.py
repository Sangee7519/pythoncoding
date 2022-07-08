#python programing to append,delete and display the element of the list usign class
class student():
	def __init__(self):
		self.n=[]
	def add(self,a):
		return self.n.append(a)
	def delete(self,b):
		return self.n.remove(b)
	def dis(self):
		return self.n
obj=student()
while True:
	print("0.Exit")
	print("1.add")
	print("2.delete")
	print("3.display")
	choice=int(input("enter the choice:"))
	if choice==1:
		n=int(input("add list:"))
		obj.add(n)
		
	elif choice==2:
		n=int(input("remove list:"))
		obj.delete(n)

	elif choice==3:
		print("list",obj.dis())
    else:
	    print("thankyou")