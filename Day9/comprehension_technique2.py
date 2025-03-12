'''
    WAP in Python to create dictonary of square of first 10 natural number
'''
'''
d={}
for i in range(1,11):
    d[i]=i**2

print(d)
'''
#Comprehension_technique

print({i:i**2 for i in range(1,11)})
