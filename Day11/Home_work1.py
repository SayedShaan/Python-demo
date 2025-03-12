'''
    WAP in python to create lambda expression for following function:

	1) average(a,b,c,d,e)
	2) max(a,b)
	3) min(a,b,c)
	
'''
'''
def average(a,b,c,d,e):
    return (a+b+c+d+e)/5
'''
average=lambda a,b,c,d,e:(a+b+c+d+e)/5
print(average(4,5,6,7,1))

'''
def max(a,b):
    if(a>b):
        return a
    else:
        return b
'''
max = lambda a,b:a if a>b else b   
print(max(5,8))
'''
def min(a,b,c):
    if(a<b and a<c):
        return a
    elif(b<a and b<c):
        return b
    else:
        return c
'''
minimum=lambda a,b,c : a if(a<b and a<c) else (b if(b<a and b<c) else c)  
print(minimum(5,8,1))













