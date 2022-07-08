#swap any two numbers in python
def swap(s,p1,p2):
	s[p1],s[p2]=s[p2],s[p1]  
	return s
s=[1,2,3,4,5]
p1=1
p2=2
print(swap(s,p1,p2))