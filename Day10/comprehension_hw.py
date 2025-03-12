'''
    Comprenhenion Tech
'''
'''
L=[]
for i in range(3):
    
    n=int(input("Enter a number"))
    L.append([i for i in range(1,n+1)])

print(L)
'''


n=int(input("How may Number you want to store"))
print("enter "+str(n)+"numbers")
print([int(input()) for i in range(1,n+1)])

#Without Comprehension 
'''
L=[]
for i in range(1,n+1):
    L.append(int(input()))

print(L)
'''
