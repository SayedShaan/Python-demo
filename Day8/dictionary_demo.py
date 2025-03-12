'''
    WAP in python two accept two number and
    create table of number in dictionary
'''
d={}
print("Enter two number ")
for i in range(2):
    n=int(input())
    d[n]=[]
    for j in range(1,11):
        d[n].append(n*j)

print(d)
    
