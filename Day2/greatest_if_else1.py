'''
    WAP in Python to accept three numbers from user and print greatest

    let a,b and c be three number

    a>b and a>c
    b>a and b>c
    c>a and c>b
'''
a=int(input("Enter First number"))
b=int(input("Enter Second number"))
c=int(input("Enter Third number"))

if(a>b and a>c):
    print(a,"is greatest")
elif( b>c):
    print(b," is greatest")
else:
    print(c,"is greatest")
