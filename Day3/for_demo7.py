'''
    WAP in Python to accept a number from user and print factorial.

    n=5! = 5*4*3*2*1 = 120
    
'''

x=int(input("Enter the number"))
y=1
for i in range(1,x+1):
    y=y*i

print("Factorial:",y)
