#Python program to reverse a number with explanation
#Suppose if someone gives input 123 and our program should give output 321.
n =12345
print("before reverse :",n)
reverse = 0
while n!=0:
    reverse = reverse*10 + n%10  
    n = (n//10) 
print("After reverse :",reverse) 