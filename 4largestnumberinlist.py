#python program to find the largest number in a list
a=[1,2,423,34,222,1212]
a.sort()
ln=a[-1]
sn=a[0]
bn=a[-2]
print("largest number in list",ln)
print("smallest number in list",sn)
print("largest secound number in list",bn)

#largest number
a=[]
n=int(input("enter the number:"))
for i in range(n):
	b=int(input("enter the number :"))
	a.append(b)
a.sort()
print(a)
print("largest number a",a[n-1])	
#secound largest number
print("largest number a",a[n-2])