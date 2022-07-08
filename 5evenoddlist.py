#find the odd or even in given list 
list1=[]
a=int(input("Enter the number:"))
for i in range(a):
	a=int(input("Enter the number :"))
	list1.append(a)
print(list1)
even=[]
odd=[]
for i in list1:
	if i%2==0:
		even.append(i)
	else:
		odd.append(i)
print("even number in list",even)
print("odd number in list",odd)

