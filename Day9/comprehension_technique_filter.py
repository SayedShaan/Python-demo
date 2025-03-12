'''
    Filter Function
'''


print(1)
L1=[2,3,1,5,4]

def even(n):
    return n%2==0

print([i for i in filter(even,L1)])

#odd
print(2)
L1=[2,3,1,5,4]

def odd(n):
    return n%2!=0

print([i for i in filter(odd,L1)])

print(3)
#Boolen Answer
L1=[2,3,1,5,4]

def even(n):
    return n%2==0

print([i for i in map(even,L1)])

print(4)
#Type Function

L1=[2,3,1.2,5,4.5]

def even(n):
    return type(n)==int

print([i for i in filter(even,L1)])


print(5)

L1=[2,3,1,5,4]

print([i for i in filter(lambda n:n%2==0,L1)])













