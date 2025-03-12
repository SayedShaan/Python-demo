'''
    Inheritance
'''
class animal:

    def foodHabits(self):       #Parent, Base
        pass

    def nooflegs(self):
        print("4 legs")



class Carnivorous(animal):              #Child, Derived 
    def foodHabits(self):
        print("Carnivorus eats only meat")

class Herbivorous(animal):              #Child, Derived
    def foodHabits(self):
        print("Herbivourous eats only plants")


c=Carnivorous()
c.foodHabits()
c.nooflegs()

h=Herbivorous()
h.foodHabits()
h.nooflegs()
