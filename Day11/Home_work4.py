'''
   WAP in python to create three list for three subjects:
and display total marks and percentage  
'''

s1=[59,89,78]
s2=[69,59,78]
s3=[79,69,99]

def average(a,b,c):
    return(a+b+c)/3

def percentage(a,b,c):
    return (a+b+c)/300*100

print()
print([i for i in map(average,s1,s2,s3)])
print([i for i in map(lambda a,b,c:(a+b+c)/3,s1,s2,s3)])
print()
print([i for i in map(percentage,s1,s2,s3)])
print([i for i in map(lambda a,b,c:(a+b+c)/300*100,s1,s2,s3)])

print()

print(sum(s1)/len(s1))
print(sum(s2)/len(s2))
print(sum(s3)/len(s3))

print()

L1=[s1,s2,s3]

for i in L1:
    print(sum(i)/len(i))













    

