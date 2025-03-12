'''
    Delete product
'''
def delete():
    import sqlite3

    prid=int(input("Enter the product Id"))

    con=sqlite3.connect("mydb.db")
    con.execute("delete from products where productid=?",(prid,))
    con.commit()

    print("Product deleted Successfully!!!!!!!!")

