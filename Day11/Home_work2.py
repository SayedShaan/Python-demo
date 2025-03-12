'''
    WAP in Python to create following classes:

	Employee
		Hours Variable
		ShowWorkingHourse() Function
		
	PartTimeEmployee
	FullTimeEmployee
'''

class employee():
    '''
    def __init__(self,hours):
        self.hours=hours
    '''
    hours=0 
    def showWorkingHours(self):
        pass

class PartTimeEmployee(employee):

    def showWorkingHours(self):
        hours=4
        print("part time employee hours:",hours)


class FullTimeEmployee(employee):

    def showWorkingHours(self):
        hours=8
        print("Full time employee hours:",hours)




pte=PartTimeEmployee()
fte=FullTimeEmployee()

pte.showWorkingHours()
fte.showWorkingHours()
                     











