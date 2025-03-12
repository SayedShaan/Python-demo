'''
 WAP in python to accept height from and check whether height is greater
    than or equal to 4 then print appropriate message.
'''

height = int(input("Enter the height \n"))

if(height>=1 and height<=8):
    if(height>=4):
        print("Eligible")
    else:
        print("not eligible")
else:
    print("invalid Height")
