'''
    select data
'''
def select():
    import sqlite3

    con=sqlite3.connect("mydb.db")
    rows=con.execute("select productid,productname from products")


    for row in rows:
        print("Product id:",row[0])
        print("Product name:",row[1])
        print()
