'''
    WAP in Python to accept five name from user and store in tuple
'''

t=()#(Shaan,Ankita,Sonia,Ravi,Janvi)
print("Enter five name")

for i in range(5):
    t=t+(input(),)#(Shaan,)+(Ankita,)+(Sonia,)+(Ravi,)+(Janvi,)

print(t)
