'''
    Resursion 
'''
'''
def fun(i):
    i+=1
    print("NIIT")
    if(i!=10):
      fun(i)
'''  
def fun(i):
    i+=1
    print("NIIT")
    if(i!=10):
        return
    
    fun(i)    
#call function fun
fun(1)
