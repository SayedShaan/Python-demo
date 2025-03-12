'''
r  ->read
w  ->write
a  ->append
r+ ->read,append
w+ ->write,read
a+ ->append,read
rb ->read, binary
wb ->write,binary
'''
import os

f1=open("D:\\logo.png","rb")
os.mkdir("D:\\images\\")
f2=open("D:\\images\logo.png","wb")


f2.write(f1.read())

f1.close()
f2.close()

os.remove("D:\\logo.png")
print("File copied sucessfully!!!!")
