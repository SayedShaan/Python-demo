'''
    Classes & Objects
'''

class Employee:

    employeeid= 0
    employeename=""

#Here e1,e2 are called objects
e1=Employee()#constructor
e2=Employee()#constructor

e1.employeeid=123
e1.employeename="Suresh"


e2.employeeid=124
e2.employeename="Ramesh"


print("=========Employee Details 1 ==========\n")
print("Employee Id : ", e1.employeeid)
print("Employee Id : ",e1.employeename)

print("=========Employee Details 2 ==========\n")
print("Employee Id : ", e2.employeeid)
print("Employee Id : ", e2.employeename)
