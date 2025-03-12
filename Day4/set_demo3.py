'''
    WAP in python to take five name from user and print
    random winner
'''

s=set()
print("Enter Five name")

for i in range(5):
    s.add(input()) # add function is comming from sets


print(s)

for i in s:
    print("Winner is :",i)
    break
