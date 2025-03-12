'''
    insert data
'''
def insert():
    import sqlite3

    pid=int(input("Enter product id"))
    pnm=input("Enter product name")

    con=sqlite3.connect("mydb.db")
    con.execute("insert into products values(?,?)",(pid,pnm))
    con.commit()

    print("Product inserted successfully!!!!!")
