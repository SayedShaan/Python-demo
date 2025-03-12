 
class Circle:
 

    def __init__(self,radius):
        self.radius=radius

    def __add__(self,another_circle):
        return self.radius + another_circle.radius

    def __sub__(self,another_circle):
        return self.radius - another_circle.radius

    def __mul__(self,another_circle):
        return self.radius * another_circle.radius

    def __truediv__(self,another_circle):
        return self.radius / another_circle.radius

    def __floordiv__(self,another_circle):
        return self.radius // another_circle.radius

    def __mod__(self,another_circle):
        return self.radius % another_circle.radius

    def __gt__(self,another_circle):
        return self.radius > another_circle.radius

    def __lt__(self,another_circle):
        return self.radius < another_circle.radius

    def __ge__(self,another_circle):
        return self.radius >= another_circle.radius

    def __le__(self,another_circle):
        return self.radius <= another_circle.radius

    def __eq__(self,another_circle):
         return self.radius == another_circle.radius

    def __ne__(self,another_circle):
         return self.radius != another_circle.radius

     

'''
c1=Circle()
c1.radius=6

c2.Circle()
c2.radius=7
'''

c1=Circle(6)
c2=Circle(7)


print(c1.radius+c2.radius)

print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1//c2)
print(c1%c2)
print(c1>c2)
print(c1<c2)
print(c1>=c2)
print(c1<=c2)
print(c1==c2)
print(c1!=c2)

