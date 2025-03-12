'''
    Update Product
'''
def update():
    import sqlite3

    pid=int(input("Enter product id"))
    pname=input("Enter new product name")


    con=sqlite3.connect("mydb.db")
    con.execute("update products set productname=? where productid=?",(pname,pid))
    con.commit()


    print("Product updated successfully!!!!!")
