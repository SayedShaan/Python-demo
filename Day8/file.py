'''
    WAP in Python 
'''

bookname=input("Enter book name")#Harry Potter
author=input("Enter author")#J.K Rowling
price=input("Enter price")#800

f=open(bookname+".txt","w")
f.write("Book name:"+bookname +"\n")
f.write("Book author:"+author+"\n")
f.write("Book Price:"+price+"\n")
f.close()

print("Save book successfully")


