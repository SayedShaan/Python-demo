'''
    Dictionary
'''

#Empty Distionary

d={}
print(d)
print(type(d))


a=2
b=2.2

print(type(a))
print(type(b))


#Dictionary with key, values


products={"P001":"Blue Polo Shirt","P002":"Black Polo Shirt","P001":"Duke hat"}
print(products["P001"])

print()

#update Black Polo shirt to yellow shirt
products["P002"]="Yellow Polo Shirt"
print(products)

products["P003"]="White Polo Shirt"
print(products)
#Dictionary doesn't Support indexing
print()
print(products["P001"])
print(products["P002"])
print(products["P003"])


#Dictionary is heterogenous

d={1:1.1,"2":True,False:5}
print(d)

#Dictionary Functions
print(products.keys())
print(products.values())
print(products.items())


#iterate over keys
print()
for i in products.keys():
    print(i)

    
#iterate over values
print()
for i in products.values():
    print(i)

    
#iterate over keys,values
print()
for i,j in products.items():
    print(i,j)

    

