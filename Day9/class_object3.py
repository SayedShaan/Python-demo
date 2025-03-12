z=9                     #Global Variable

class Myclass:

    a=2                 #Member Variable
    b=3                 #Member Variable

    def function1(self):

        a=3             # Local, Function  Variable
        print(a)        # 3
        print(self.a)   # 2
        print(self.b)   #3
        print(z)        #9

    def function2(self):
        #print(a)        #Error
        print(self.a)   #2
        print(self.b)   #3
        print(z)        #9

    def add(self,a,b):
        print("Addition: ",a+b) #5
        print(z)        #9

class Myclass2:

    def function3(self):
        print(z)        #9
        
    
#2nd way to call function 
m1=Myclass()
m1.function1()
m1.function2()
m1.add(2,3)

m2=Myclass2()
m2.function3()


