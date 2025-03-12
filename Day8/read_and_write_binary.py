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


f1=open("D:\\logo.png","rb")
f2=open("D:\shaan\logo.png","wb")

f2.write(f1.read())

f1.close()
f2.close()


print("File copied sucessfully!!!!")
