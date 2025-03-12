'''
    List
'''

#List is Ordered, mutable , heterogenous

#Empty List
L=[]
print(L)


#List with values
L=[1,2,3,4,5]
print(L)

#indexing
print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[4])


# For Loop
print()
for i in range(5):
    print(L[i])

#foreach
print()
for i in L:
    print(i)

#List is mutable
print()
L[4]=7
print(L)

#Heterogenous
print()
L=[1,1.4,"Shaan",True]
print(L)


#Append Vs Extend

print()
L1=[1,2,3]
L2=[4,5,6]

L1.append(L2)
print(L1)

print()
L1=[1,2,3]
L2=[4,5,6]

L1.extend(L2)
print(L1)

print()
L1=[1,2,3]
L2=[4,5,6]

#Add list as nested list using append function
L1.append(L2)
#You can add sing value in list using append function 
L1.append(5)
print(L1)

print()
L1=[1,2,3]
L2=[4,5,6]

L1.extend(L2)
#You cannot add a single value in list using Extend function
#L1.extend(5)

#you can add and take individual values from list using extend function
L1.extend([5])
print(L1)


#List Function
print()
#ASC
L1=[2,3,6,4,5]
L1.sort()
print(L1)

print()
#DESC
L1=[2,3,6,4,5]
L1.sort()
L1.reverse()
print(L1)

print()
#LIFO - Last in First Out
L1=["Nokia","Samsung","Iphone","Oppo","Vivo","OnePlus"]
L1.reverse()
print(L1)

print()
#Sort date in descending Order
L1=[2,3,4,8,1,5]
L1.sort(reverse=True)
print(L1)

print()
#Slicing
#First Paremeter - Start Value
#Second Paremate - Stop Value
#Third Paremeter-  Stride value / Step value


L1=[4,5,6,7,1,3]
print(L1)

#Traverse from left to right
print(L1[3])
print(L1[2:5])
print(L1[1:3])
print(L1[3:6])
print(L1[1:6:2])
print(L1[::1])
print(L1[::])

#Traverse from right to left 
print(L1[-1])
print(L1[-1:-4:-1])
print(L1[-1:-7:-1])#Stride value or step value
print(L1[-1:-7:-2])
print(L1[-1::-1])
print(L1[::-1])
print(L1[::])

#Length Function
#Length Function is Common in Tuple,Set,List,Dictionary

L1=[2,3,4,1,5]
print(len(L1))





























































