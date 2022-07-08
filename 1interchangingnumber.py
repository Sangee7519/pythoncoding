#interchaing the first and last number in python
#apporach1
def swap(newlist):# function
	size=len(newlist) # lenth of list
	a=newlist[0] 
	newlist[0]=newlist[size-1]
	newlist[size-1]=a
	return newlist # return the list
newlist=[12,35,9,56,24]
print(swap(newlist)) # print the list
#apporach2
def swap(s):
	a=s[0]
	s[0]=s[-1]
	s[-1]=a
	return s
s=[1,2,3,4]
print(swap(s))

#apporach3
def swap(s):
	get=s[0],s[-1]
	print(get)
	s[-1],s[0]=get
	print(s[-1],s[0])
	return s
s=[1,2,3,4,5]
print(swap(s))

#apporach4
def swap(s):
	a,*b,c=s
	s=[*b]
	return s

s=[1,2,3,4,3]
print(swap(s))	



