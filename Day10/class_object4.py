'''
    Classes & Objects
'''

class Product:

    productid=0
    productname=""
    price=0.0

class ProductOperations:

    products=[]

    def addProducts(self):
        
        for i in range(3):
            p=Product()
            p.productid=int(input("Enter the product id"))#123
            p.productname=input("Enter the product name")#iphone
            p.price=float(input("Enter the product price"))#45689
            print()

            self.products.append(p)
        

    def displayProducts(self):#(self)is Declared outside the function 

        for p in self.products:
            print("Product Id:",p.productid)
            print("Product Name:",p.productname)
            print("Price:",p.price)
            print()

    
po=ProductOperations()
po.addProducts()
po.displayProducts()










        
