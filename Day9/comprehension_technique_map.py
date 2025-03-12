'''
    MAP Function 
'''
L1=[2,3,4]
L2=[4,5,1]

'''
L3=[]#[6,8,5]
for i,j in zip(L1,L2):#(2,4),(3,5),(4,1)
    L3.append(i+j)

print(L3) 
'''
'''
def sum(a,b):
    return a+b

print([i for i in map(sum,L1,L2)])
'''

print([i for i in map(lambda a,b:a+b,L1,L2)])
