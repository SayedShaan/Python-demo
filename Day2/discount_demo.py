'''
    WAP in Python to accept amount from user  and check whether amount
    is greater than 5000 and print discoun.

    Note: Amount above 5000 will get 5% discount
'''

amount=int(input("Enter the amount \n"))
if(amount>5000):
               print("Discount:",0.05*amount)
else:
               print("no discount")
           
