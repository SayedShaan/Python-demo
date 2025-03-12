'''
    Calculator
'''

def add(a,b):
    print("Addition:",a+b)

def sub(a,b):
    print("subtraction:",a-b)

def div(a,b):
    print("Division:",a/b)

def mul(a,b):
    print("Multiplication:",a*b)
'''
def choice():
    ch=input("Do you want to continue with this app")
    if(ch=="yes"):
        menu()
'''

#Recursion
def menu():
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))

    print("==Menu==")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    ch=int(input("Enter your choice"))


    if(ch==1):
       add(a,b)
    elif(ch==2):
        sub(a,b)
    elif(ch==3):
        mul(a,b)
    elif(ch==4):
        div(a,b)
    else:
        print("Invalid option!!!!!!!!!")
        
    ch=input("Do you want to continue with this app")
    if(ch=="yes"):
        menu()

                
menu() 













            


