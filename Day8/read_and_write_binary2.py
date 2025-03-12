'''
    File Function
    -tell
    -seek

    Seek Function
        0 - beginning position
        1 - current position
        2 - end position
'''
txt=open("foo.txt","rb")
print(txt.tell())
print()

txt.seek(2)
print(txt.tell())#2
print(txt.read())#llow world

print()
txt.seek(2,0)
print(txt.tell())#2
print(txt.read())#llo world

print()
txt.seek(2,0)
txt.seek(2,1)
print(txt.tell())#4
print(txt.read())#o world

print()
txt.seek(-5,2)
print(txt.tell())#6
print(txt.read())#world

