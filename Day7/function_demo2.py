'''
    Factorial of 5

    5!=5*4*3*2*1
'''
# Factorial using recursion
def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

#Using Loop
'''
p=1
for i in range(5,0,-1):
    p=p*i
print(p)
'''
