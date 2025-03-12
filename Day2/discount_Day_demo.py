'''
    WAP in Python to accept amount and day from user  and check whether amount
    is greater than 5000 and  day is sunday  then print discoun.

    Note: Amount above 5000 will get 5% discount
'''

amount=float(input("Enter the amount \n"))
day=input("Enter the day\n").lower()#lower() is function to convert the into lowercase or upper() uppercase
if(amount>5000 and day=="sunday"):
               print("Discount:",0.05*amount)
else:
               print("no discount")
           
