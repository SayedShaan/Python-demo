'''
    WAP in Python to accept a number from a user and
    print table of the number
    n=5

    5
    10
    15
    20
    .
    .
    50
'''

n=int(input("Enter the number "))
count=1
while(count<=10):
    print(n*count,end=" ")'by default it is a new line end = space '
    count=count+1
