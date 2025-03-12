'''
    Tuple
'''
#Tuple is ordered ,immutable, heterogenous and dynamic  

#Empty Tuple
t=()
print(t)

#Tuple with values
t=(2,3,4,1,5)
print(t)

print()

#Indexing
print(t[2])
print(t[4])

print()

#Indexing in order 
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])

print()
#For loop
for i in range(0,5):
    print(t[i])

print()
#Foreach Loop
for i in t:
    print(i)

'''
#it is immutable
t[2]=44
print(t)
'''
#heterogenous

t=(1,1.1,"Sameer",True)
print(t)


#

t1=(2,3,4)
t2=(3,4,5)

t3=t1+t2
print(t3)












    
