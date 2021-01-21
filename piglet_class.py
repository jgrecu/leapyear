class Piglet:
    """Class to create a pig."""
    def __init__(self, name, years):
        self.name = name
        self.years = years
    
    def __str__(self):
        return "This pigglet name is {} and it's age is {}".format(self.name, self.years*18)
    
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))
    
    def pig_years(self):
        return self.years * 18

# hamlet = Piglet("Hamlet", 2)
# hamlet.speak()

# petunia = Piglet("Petunia", 2)
# petunia.speak()
# print(petunia)
