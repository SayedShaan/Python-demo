import sys
sys.path.insert(1,'D:\\SQL\\')

import insert_data
import delete_data
import update_data
import select_data

def menu():
    print("====Menu===")
    print("1. Add Product")
    print("2. Delete Product")
    print("3. Update Product")
    print("4. Display Product")
    n=int(input("Select one option"))

    if(n==1):
        insert_data.insert()
    elif(n==2):
        delete_data.delete()
    elif(n==3):
        update_data.update()
    elif(n==4):
        select_data.select() 
    else:
        print("invalid option!!!!")

    ch=input("Do you want to continue with this app")
    if(ch=="yes"):
        menu()

menu()       
