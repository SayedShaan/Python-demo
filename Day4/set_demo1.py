'''
    SET
'''
#Set is Unordered

#Empty set
s=set()
print(s)

#Set with value
#By default numeric data is sorted in ascending order
#It will not allow any duplicate values

s={2,1,3,5,2,0}
print(s)

#indexing is not possible
#print(s[0])


# set is heterogenous

s={1,1.2,"A"}
print(s)

# set is immutable
#we cannot change the values in immutable 
#s[0]=22

# For String values it is gives output in random order
s={"A","C","D","B"}
print(s)


