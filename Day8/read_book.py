import glob # search the name of the file from the folder glob

print("***Files Available***")
files=glob.glob("*.txt")
for file in files:
    print(file)

print()
#opening the file 
bookname=input("Enter book name")
f=open(bookname+".txt")
print(f.read())
f.close()


