'''
    Database Software -SQLITE
    SQL - Structured Query Language

    Create Database & Table
'''

import sqlite3

con=sqlite3.connect("mydb.db")
con.execute(
            '''
                create table products
                (
                    productid int,
                    productname text
                )
            ''')  

print("Database & table created Successfully!!!!!!!!")    
