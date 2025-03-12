'''
    WAP in python to accpt five number from user and display even number 
'''

L1=[]

print("Enter Three number")

for i in range(3):
    L1.append(int(input()))

for i in L1:
    if (i%2==0):
        print(i)
'''
L1=[2,3]

print("Enter Three number")

for i in range(3):
    L1.append(int(input()))

for i in L1:
    if (i%2==0):
        print(i)
'''
