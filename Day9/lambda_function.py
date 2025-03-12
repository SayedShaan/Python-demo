'''
    Lambda expression 
'''
'''
def square(n):
    return n**2

print(square(2))
'''
'''
def factorial(n):
    if(n==1):
        return 1
    else:
      return n * factorial(n-1)
'''
factorial=lambda n:1 if(n==1) else n* factorial(n-1)
square=lambda n:n**2 if(n>0) else "invalid number"
cube=lambda n:n**3

print(square(-2))
print(cube(3))
print(factorial(4))

