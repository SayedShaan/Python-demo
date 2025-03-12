'''
    WAP in Python to call calculate Gross Salary,

    BS<10000  HRA=95% DA=95%
    BS>=10000 HRA=90% DA=90%
    BS>=20000 HRA=80% DA=85%

    Gross Salary = HRA+DA+Basic Salary 
'''

amt=int(input("Enter Your Salary"))
if(amt>=2000):
    hra=amt*0.8
    da=amt*0.85
elif(amt>=10000):
    hra=amt*0.9
    da=amt*0.9
elif(amt<10000):
    hra=amt*0.95
    da=amt*0.95
print("Salary :",amt,"\nHRA",hra,"\nDA",da,"\nGross Salary :",amt+da+hra)
